"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase


# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_truetest(self):
        test = True
        self.assertTrue(test)

    def test_falsetest(self):
        test = False
        self.assertFalse(test)
    
    def test_lasttest(self):
        test1 = 5
        test2 = 5        
        self.assertEqual(test1, test2)
    
    def test_somemoretests(self):
        hoi = "lol"
        self.assertEqual(hoi, "lol")

    
