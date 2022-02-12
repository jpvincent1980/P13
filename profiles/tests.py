from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Profile


# Create your tests here.
class IndexTest(TestCase):
    """
    A class that gathers tests for the profiles list view.
    """
    def test_status_code(self):
        """
        Tests that the view returns a 200 status code.
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        """
        Tests that the view uses the correct template.
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_title(self):
        """
        Tests that 'Profiles' is included in the returned HTML
        inside a <title></title> tag.
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertContains(response, "<title>Profiles</title>")


class IndexNoProfileTest(TestCase):
    """
    A class that gathers tests for the profiles list view when
    no profile exists.
    """
    def test_status_code(self):
        """
        Tests that the view returns a 200 status code.
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        """
        Tests that the view uses the correct template.
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_title(self):
        """
        Tests that the sentence 'No profiles are available.' is included
        in the returned HTML inside a <p></p> tag.
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertContains(response, "<p>No profiles are available.</p>")


class ProfileTest(TestCase):
    """
    A class that gathers tests for the lettings detail view.
    """
    username = "John Steed"

    @classmethod
    def setUpTestData(cls):
        """
        User and Profile instances are created to run the upcoming tests.
        """
        # Creates a user and a profile associated to that user for the tests
        user = User.objects.create(username=cls.username)
        cls.profile = Profile.objects.create(user=user)

    def test_profile_status_code(self):
        """
        Tests that the view returns a 200 status code.
        """
        response = self.client.get(reverse('profiles:profile',
                                           kwargs={"username": ProfileTest.username}))
        self.assertEqual(response.status_code, 200)

    def test_profile_template_used(self):
        """
        Tests that the view uses the correct template.
        """
        response = self.client.get(reverse('profiles:profile',
                                           kwargs={"username": ProfileTest.username}))
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_title(self):
        """
        Tests that the profile username is included in the returned HTML
        inside a <title></title> tag.
        """
        response = self.client.get(reverse('profiles:profile',
                                           kwargs={"username": ProfileTest.username}))
        self.assertContains(response, "<title>"+ProfileTest.username+"</title>")
