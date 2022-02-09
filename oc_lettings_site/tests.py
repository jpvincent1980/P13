from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class IndexTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')

    def test_title(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, "<title>Holiday Homes</title>")
