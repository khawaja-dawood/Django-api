import os
import shutil
import tempfile
from PIL import Image # pip install pillow

from django.urls import reverse
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from rest_framework_jwt.settings import api_settings


jwt_payload_handler             = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              = api_settings.JWT_ENCODE_HANDLER
User = get_user_model()


class PostTestCase(TestCase):
    def setUp(self): 
        user = User.objects.create(username='f18bb128', email='f18bb128@ibitpu.edu.pk')
        user.set_password("Spotify420")
        user.save()

    def test_creating_post(self):
        user = User.objects.get(username='f18bb128')
        obj = Post.objects.create(owner=user, description='Some cool new content')
        self.assertEqual(obj.id, 1)
        qs = Post.objects.all()
        self.assertEqual(qs.count(), 1)


class PostAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='f18bb129', email='f18bb129@ibitpu.edu.pk')
        user.set_password("Spotify420")
        user.save()
        status_obj = Post.objects.create(user=user, content='Hello there!')

    def test_statuses(self):
        self.assertEqual(Post.objects.count(), 1)

    def status_user_token(self):
        auth_url = api_reverse('api-user:login')
        auth_data = {
            'username': 'f18bb129',
            'password': 'Spotify420',
        }
        auth_response = self.client.post(auth_url, auth_data, format='json')
        token = auth_response.data.get("token", None)
        if token is not None:
            self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

    def create_item(self):
        self.status_user_token()
        url = api_reverse('api-core:get-posts')
        data = {
            'description': "some cool test content"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        return response.data

    def test_empty_create_item(self):
        self.status_user_token()
        url = api_reverse('api-core:get-posts')
        data = {
            'description': None,
            'image': None
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        return response.data

    def test_status_create_with_image(self):
        self.status_user_token()
        url = api_reverse('api-core:get-posts')
        # (w, h) = (800, 1280)
        # (255, 255, 255)
        image_item = Image.new('RGB', (800, 1280), (0, 124, 174))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image_item.save(tmp_file, format='JPEG')
        with open(tmp_file.name, 'rb') as file_obj:
            data = {
                'description': "some cool test content",
                'image': file_obj
            }
            response = self.client.post(url, data, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Post.objects.count(), 2)
            img_data = response.data.get('image')
            self.assertNotEqual(img_data, None)
        temp_img_dir = os.path.join(settings.MEDIA_ROOT, 'tempMedia', 'tempImages')
        if os.path.exists(temp_img_dir):
            shutil.rmtree(temp_img_dir)

    def test_status_create_with_img_and_desc(self):
        self.status_user_token()
        url = api_reverse('api-core:get-posts')
        # (w, h) = (800, 1280)
        # (255, 255, 255)
        image_item = Image.new('RGB', (800, 1280), (0, 124, 174))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image_item.save(tmp_file, format='JPEG')
        with open(tmp_file.name, 'rb') as file_obj:
            data = {
                'description': None,
                'image': file_obj
            }
            response = self.client.post(url, data, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            self.assertEqual(Post.objects.count(), 2)
        temp_img_dir = os.path.join(settings.MEDIA_ROOT, 'tempMedia', 'tempImages')
        if os.path.exists(temp_img_dir):
            shutil.rmtree(temp_img_dir)

    def test_status_create(self):
        data = self.create_item()
        data_id = data.get("id")
        rud_url = api_reverse('api-core:upd-del', kwargs={"id": data_id})
        rud_data = {
            'description': "another new content"
        }

        '''
        get method / retrieve
        '''
        get_response = self.client.get(rud_url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

    def test_status_update(self):
        data = self.create_item()
        data_id = data.get("id")
        rud_url = api_reverse('api-core:upd-del', kwargs={"id": data_id})
        rud_data = {
            'description': "another new content"
        }
        '''
        put / update
        '''
        put_response = self.client.put(rud_url, rud_data, format='json')
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)
        rud_response_data = put_response.data
        self.assertEqual(rud_response_data['description'], rud_data['description'])

    def test_status_delete(self):
        data = self.create_item()
        data_id = data.get("id")
        rud_url = api_reverse('api-core:upd-del', kwargs={"id": data_id})
        rud_data = {
            'description': "another new content"
        }
        '''
        delete method / delete
        '''
        del_response = self.client.delete(rud_url, format='json')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)
        '''
        Not found
        '''
        get_response = self.client.get(rud_url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_status_no_token_create(self):
        url = api_reverse('api-core:get-posts')
        data = {
            'description': "some cool test content"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_other_user_permissions_api(self):
        data = self.create_item()
        data_id = data.get("id")
        user = User.objects.create(username='testjmitch')
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        rud_url = api_reverse('api-core:upd-del', kwargs={"id": data_id})
        rud_data = {
            'description': "smashing"
        }
        get_ = self.client.get(rud_url, format='json')
        put_ = self.client.put(rud_url, rud_data, format='json')
        delete_ = self.client.delete(rud_url, format='json')
        self.assertEqual(get_.status_code, status.HTTP_200_OK)
        self.assertEqual(put_.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(delete_.status_code, status.HTTP_403_FORBIDDEN)