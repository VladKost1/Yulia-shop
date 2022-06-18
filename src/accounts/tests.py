from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class TestUser(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = get_user_model().objects.create(email="vladkostiuk2@gmail.com")
        self.user.set_password("12345")
        self.user.save()

        self.admin = get_user_model().objects.create(email="admin@gmail.com", is_staff=True)
        self.admin.set_password("12345")
        self.admin.save()

    def test_user_login_wrong_email(self):
        user_login = self.client.login(email="wrong_email", password="12345")
        self.assertFalse(user_login)

    def test_user_access(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_user_access_admin_panel(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 302)

    def test_admin_access_admin_panel(self):
        self.client.force_login(self.admin)
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, 200)
