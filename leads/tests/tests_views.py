from django.test import TestCase
from django.shortcuts import reverse


# Create your tests here.

class HomepageTest(TestCase):

    def test_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/landing-page.html')