from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


# Create your tests here.
class IndexTest(TestCase):
    """
    A class that gathers tests for the lettings list view.
    """
    def test_status_code(self):
        """
        Tests that the view returns a 200 status code.
        """
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        """
        Tests that the view uses the correct template.
        """
        response = self.client.get(reverse('lettings:index'))
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_title(self):
        """
        Tests that 'Lettings'' is included in the returned HTML
        inside a <title></title> tag.
        """
        response = self.client.get(reverse('lettings:index'))
        self.assertContains(response, "<title>Lettings</title>")


class IndexNoLettingTest(TestCase):
    """
    A class that gathers tests for the lettings list view when
    no letting exists.
    """
    def test_status_code(self):
        """
        Tests that the view returns a 200 status code.
        """
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        """
        Tests that the view uses the correct template.
        """
        response = self.client.get(reverse('lettings:index'))
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_title(self):
        """
        Tests that the sentence 'No lettings are available.' is included
        in the returned HTML inside a <p></p> tag.
        """
        response = self.client.get(reverse('lettings:index'))
        self.assertContains(response, "<p>No lettings are available.</p>")


class LettingTest(TestCase):
    """
    A class that gathers tests for the lettings detail view.
    """
    letting_title = "Nantes"
    letting_number = 1
    letting_zip_code = 44000

    @classmethod
    def setUpTestData(cls):
        """
        Address and Letting instances are created to run the upcoming tests.
        """
        # Creates an address and a letting for the tests
        address = Address.objects.create(number=cls.letting_number,
                                         zip_code=cls.letting_zip_code)
        cls.letting = Letting.objects.create(title=cls.letting_title,
                                             address=address)

    def test_letting_status_code(self):
        """
        Tests that the view returns a 200 status code.
        """
        response = self.client.get(reverse('lettings:letting',
                                           kwargs={"letting_id": 1}))
        self.assertEqual(response.status_code, 200)

    def test_letting_template_used(self):
        """
        Tests that the view uses the correct template.
        """
        response = self.client.get(reverse('lettings:letting',
                                           kwargs={"letting_id": 1}))
        self.assertTemplateUsed(response, 'lettings/letting.html')

    def test_letting_title(self):
        """
        Tests that the letting title is included in the returned HTML
        inside a <title></title> tag.
        """
        response = self.client.get(reverse('lettings:letting',
                                           kwargs={"letting_id": 1}))
        self.assertContains(response,
                            "<title>"+LettingTest.letting_title+"</title>")

    def test_letting_zip_code(self):
        """
        Tests that the instance zip_code is included in the returned HTML.
        """
        response = self.client.get(reverse('lettings:letting',
                                           kwargs={"letting_id": 1}))
        self.assertIn(str(LettingTest.letting_zip_code), str(response.content))
