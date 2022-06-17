from django.test import TestCase
from store.models import Author, Book, Stock
from datetime import date
from django.urls import reverse
import json


#-------------------------------------------------------------------------
#models tests

class AuthorModelTest(TestCase):

    def setUp(self):
        dob = date.today()
        Author.objects.create(firstName = "john",lastName ="doe",email ="john@email.com",dob=dob)


    def test_author_name(self):
        fname = Author.objects.get(id = 1)
        expected_object_name = f'{fname.firstName}'


        self.assertEqual(expected_object_name, 'john')

class BookModelTest(TestCase):

    def setUp(self):
        dob = date.today()
        book = Author.objects.create(firstName = "john",lastName ="doe",email ="john@email.com",dob=dob)
        Book.objects.create(title = "Harry",YearOfPublication =dob,description ="this awesome book =",date_added=dob,author_id = book)


    def test_book_title(self):
        book_title = Book.objects.get(id = 1)
        expected_object_name = f'{book_title.title}'


        self.assertEqual(expected_object_name, 'Harry')


class StockModelTest(TestCase):

    def setUp(self):
        dob = date.today()
        book = Author.objects.create(firstName = "john",lastName ="doe",email ="john@email.com",dob=dob)
        stock =Book.objects.create(title = "Harry",YearOfPublication =dob,description ="this awesome book =",date_added=dob,author_id = book)
        Stock.objects.create(status ="good",date_added =dob,updated_at =dob,quantity= 1,book_id = stock)

    def test_book_title(self):
        stock_status = Stock.objects.get(id = 1)
        expected_object_name = f'{stock_status.status}'


        self.assertEqual(expected_object_name, 'good')


#--------------------------------------------------------------------------------
#view tests
class CreateAuthorTest(TestCase):
   
    def setUp(self):
        dob = date.today()
        Author.objects.create(firstName = "john",lastName ="doe",email ="john@email.com",dob=dob)


    def test_post_view(self):
        dob = date.today()
        data = {'firstName':"john",'lastName' :"doe",'email' :"john@email.com",'dob':dob}
        response = self.client.post(reverse('create_author'),data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Author.objects.count(), 2)
        
class BookTest(TestCase):
    def setUp(self):
        dob = date.today()
        book = Author.objects.create(firstName = "john",lastName ="doe",email ="john@email.com",dob=dob)
        Book.objects.create(title = "Harry",YearOfPublication =dob,description ="the boy who lived",date_added=dob, author_id=book)


    def test_post_view(self):
        dob = date.today()
         
        data = {'title':"harry",'YearOfPublication' :dob,'description' :"the boy who lived",'author_id': "1"}
        response = self.client.post(reverse('create_book'),data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 2)

    def test_list_view(self):
        response = self.client.get(reverse('create_book'))
        self.assertEqual(response.status_code, 200)
        
        self.assertContains(response,"the boy who lived")

    

    def test_get_book_view(self):
        dob = date.today()
        data = {'title':"harry",'YearOfPublication' :dob,'description' :"the boy who lived",'author_id': "1"}
        response = self.client.get(reverse('book_details',kwargs = {'pk':1}), data )
        self.assertEqual(response.status_code ,200)

    '''def test_put_book_view(self):
        dob = date.today()
        data = {'title':"harry",'YearOfPublication' :dob,'description' :"the boy who lived",'author_id': "1"}
        response = self.client.put(reverse('book_details',kwargs = {'pk':1}), data )
        self.assertEqual(response.status_code ,200)
        self.assertContains(response,"the boy who lived")'''
       

    def test_delete_view(self):
        dob = date.today()
        data = {'title':"harry",'YearOfPublication' :dob,'description' :"the boy who lived",'author_id': "1"}
        response = self.client.delete(reverse('book_details',kwargs = {'pk':1}), data )
        self.assertEqual(response.status_code ,204)



class CreateStockTest(TestCase):
    def setUp(self):
        dob = date.today()
        book = Author.objects.create(firstName = "john",lastName ="doe",email ="claire@email.com",dob=dob)
        stocks=Book.objects.create(title = "Harry",YearOfPublication =dob,description ="the boy who lived",date_added=dob, author_id=book)
        Stock.objects.create(book_id = stocks, quantity ="20")

    def test_post_view(self):
       
         
        data = {'book_id':"1",'quantity' :"20"}
        response = self.client.post(reverse('create_stock'),data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Stock.objects.count(), 1)

    def test_list_view(self):
        response = self.client.get(reverse('create_stock'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,"20")

    
    def test_get_stock_view(self):
       
        data = {'book_id':"1",'quantity' :"20"}
        response = self.client.get(reverse('stock_details',kwargs = {'pk':1}), data )
        self.assertEqual(response.status_code ,200)

    '''def test_patch_stock_view(self): 

        dob = date.today()
        author = Author.objects.create(firstName = "john",lastName ="doe",email ="claire@email.com",dob=dob)
        books = Book.objects.create(title = "Harry",YearOfPublication =dob,description ="the boy who lived",date_added=dob, author_id=author)
        stock = Stock.objects.create(book_id = books, quantity ="20") 

        data = {'book_id':"1",'quantity' :"10"}
        
        response = self.client.patch(reverse('stock_details',args = [stock.id] ), data)
        #print(response)
        self.assertEqual(response.status_code, 200)
        
        #self.assertContains(response,200)'''
       

    def test_delete_view(self):
        data = {'book_id':"1",'quantity' :"20"}
        response = self.client.delete(reverse('stock_details',kwargs = {'pk':1}), data )
        self.assertEqual(response.status_code ,204)
    

    





