from django.test import TestCase


from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='f18bb125', email='f18bb125@ibitpu.edu.pk')
        user.set_password("Spotify420")
        user.save()

    def test_created_user(self):
        qs = User.objects.filter(username='f18bb125')
        self.assertEqual(qs.count(), 1)