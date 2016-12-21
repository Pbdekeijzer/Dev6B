import django
from django.test import TestCase, Client


# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

class TemplateTest(TestCase):        
    def test_templateindex(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, "app/index.html")

    def test_templateabout(self):
        client = Client()
        response = client.get('/about')
        self.assertTemplateUsed(response, "app/about.html")

    def test_templatelogin(self):
        client = Client()
        response = client.get('/login')
        self.assertTemplateUsed(response, "app/login.html")

class ResponseTest(TestCase):           
    def test_responseindex(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_responseabout(self):
        client = Client()
        response = client.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_responselogin(self):
        client = Client()
        response = client.get('/login')
        self.assertEqual(response.status_code, 200)