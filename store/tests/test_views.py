from .test_setup import TestSetup

class TestViews(TestSetup):
    def test_cannot_create_author_with_no_data(self):
        response = self.client.post("/store/create/")
        '''import pdb
        pdb.set_trace()'''
        self.assertEqual(response.status_code,400)

    '''def test_can_create_author_with_correctly(self):
        response = self.client.post(
            self.create_url, self.author_data , format = "json")
        self.assertEqual(response.status_code,201)'''
        


'''from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from store.models import Author,Book
from store.serlializers import BookSerializer,AuthorSerializer
import datetime



class create_authorTestCase(APITestCase):
    def test_create_author(self):
        data = {"firstName":"testcase","lastName":"testcase","email":"testcase@gmail.com","dob":"2019-09-09"}
        response = self.client.post("/store/create/",data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

class create_bookTestCase(APITestCase):
    def test_create_book(self): 
        data = {"title":"testcase","YearOfPublication":"2019-09-09","description":"testcase_aannd_lo","quantity":1,"author_id": 1}
        response = self.client.post("/store/all/",data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)'''