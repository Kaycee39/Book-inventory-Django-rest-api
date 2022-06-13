from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetup(APITestCase):
    def setup(self):
        self.create_url = reverse('create author')
        self.author_data = {
            'firstName': "books",
            'lastName':"testname",
            'email':"books@gmail.com"
        }
        return super().setup()

    def tearDown(self):
        return super().tearDown()