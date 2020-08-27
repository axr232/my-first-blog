from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from blog.views import cv_page

# Create your tests here.

class CvPageTest(TestCase):

    def test_url_to_cv_page(self):
        found = resolve('/cv_page')
        self.assertEqual(found.func,cv_page)

    def test_cv_page_returns_correct_html(self):
        request = HttpRequest()
        response = cv_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith("\n<html>"))
        self.assertIn('<title> Bridging Coursework </title>',html)
        self.assertTrue(html.endswith('</html>'))
