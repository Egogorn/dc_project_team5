from django.test import TestCase

# Create your tests here.


class URLSTests(TestCase):
    def test_fake_page(self):
        response = self.client.get('/fake')
        self.assertEqual(response.status_code, 404)

    def test_profile_page(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_page(self):
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)


class FutureURLTest(TestCase):
    def test_login_page(self):
        response = self.client.get('/login_page')
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.client.get('/register_page')
        self.assertEqual(response.status_code, 200)

    def test_crete_task_page(self):
        response = self.client.get('/create_task')
        self.assertEqual(response.status_code, 200);

    def test_deadlines_page(self):
        response = self.client.get('/deadlines')
        self.assertEqual(response.status_code, 200)

    def test_deadline_page(self):
        response = self.client.get('/deadline')
        self.assertEqual(response.status_code, 200)

    def test_tasks_page(self):
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)

    def test_solutions_page(self):
        response = self.client.get('/solutions')
        self.assertEqual(response.status_code, 200)

    def test__solution_page(self):
        response = self.client.get('/solution_page')
        self.assertEqual(response.status_code, 200)

    def test_task_page(self):
        response = self.client.get('/task_page')
        self.assertEqual(response.status_code, 200)

    def test_group_page(self):
        response = self.client.get('/group_page')
        self.assertEqual(response.status_code, 200)

    def test_person_page(self):
        response = self.client.get('/person_page')
        self.assertEqual(response.status_code, 200)

    def test_create_task_page(self):
        response = self.client.get('/create_task')
        self.assertEqual(response.status_code, 200)

    def test_give_task_page(self):
        response = self.client.get('/give_task')
        self.assertEqual(response.status_code, 200)
