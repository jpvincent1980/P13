from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


# Create your tests here.
class IndexTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_title(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertContains(response, "<title>Lettings</title>")


class IndexNoLettingTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_title(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertContains(response, "<p>No lettings are available.</p>")


class LettingTest(TestCase):
    letting_title = "Nantes"
    letting_number = 1
    letting_zip_code = 44000

    @classmethod
    def setUpTestData(cls):
        # Creates an address and a letting for the tests
        address = Address.objects.create(number=cls.letting_number,
                                         zip_code=cls.letting_zip_code)
        cls.letting = Letting.objects.create(title=cls.letting_title,
                                             address=address)

    def test_letting_status_code(self):
        response = self.client.get(reverse('lettings:letting',
                                           kwargs={"letting_id": 1}))
        self.assertEqual(response.status_code, 200)

    def test_letting_template_used(self):
        response = self.client.get(reverse('lettings:letting',
                                           kwargs={"letting_id": 1}))
        self.assertTemplateUsed(response, 'lettings/letting.html')

    def test_letting_title(self):
        response = self.client.get(reverse('lettings:letting',
                                           kwargs={"letting_id": 1}))
        self.assertContains(response,
                            "<title>"+LettingTest.letting_title+"</title>")

    def test_letting_zip_code(self):
        response = self.client.get(reverse('lettings:letting',
                                           kwargs={"letting_id": 1}))
        self.assertIn(str(LettingTest.letting_zip_code), str(response.content))
