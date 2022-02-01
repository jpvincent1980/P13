from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Profile


# Create your tests here.
class IndexTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_title(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertContains(response,"<title>Profiles</title>")


class IndexNoProfileTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_title(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertContains(response,"<p>No profiles are available.</p>")


class ProfileTest(TestCase):
    username = "John Steed"

    @classmethod
    def setUpTestData(cls):
        # Creates a user and a profile associated to that user for the tests
        user = User.objects.create(username=cls.username)
        cls.profile = Profile.objects.create(user=user)

    def test_profile_status_code(self):
        response = self.client.get(reverse('profiles:profile',
                                           kwargs={"username":ProfileTest.username}))
        self.assertEqual(response.status_code, 200)

    def test_profile_template_used(self):
        response = self.client.get(reverse('profiles:profile',
                                           kwargs={"username":ProfileTest.username}))
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_title(self):
        response = self.client.get(reverse('profiles:profile',kwargs={"username":ProfileTest.username}))
        self.assertContains(response,"<title>"+ProfileTest.username+"</title>")
