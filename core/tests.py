from django.test import TestCase

# Create your tests here.

class URLSTests(TestCase):
    def test_testFakePage(self):
        response = self.client.get('/fake')
        self.assertEqual(response.status_code, 404)

    def test_testProfilePage(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)

    def test_testLoginPage(self):
        response = self.client.get('/login_page')
        self.assertEqual(response.status_code, 200)

    def test_testRegisterPage(self):
        response = self.client.get('/register_page')
        self.assertEqual(response.status_code, 200)

    def test_testDashboardPage(self):
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)