
#--------------------------------------------------------------------------
# Create your views here.
from store.serlializers import BookSerializer,AuthorSerializer,StockSerializer
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book, Stock
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend




class create_author(APIView):
        def post(self, request, format=None):
                serializer = AuthorSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class view_books(generics.ListAPIView):
    """
    List all books, or create a new book.

    """
   
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['author_id','YearOfPublication','title']

    def list(self, request, format=None):
        queryset = self.get_queryset()
        filter_backends = self.filter_queryset(queryset)

        serializer = BookSerializer(filter_backends, many=True)
                
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    """
    Retrieve, update or delete book instance.
    """
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        books = self.get_object(pk)
        serializer = BookSerializer(books)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        
        books = self.get_object(pk)
        serializer = BookSerializer(books, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        books = self.get_object(pk)
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#------------------------------------------------------------------------------------
#VIEW ALL LISTING STOCK
# ------------------------------------------------------------------------------------
class view_stock(APIView):

    
    
    def post(self,request,format=None):
        quantity = int(request.data['quantity'])
        
        if quantity <= 0:
                    my_status = "out of stock"
        elif quantity <= 5 and quantity >= 1:
                    my_status ="critical"
        elif quantity <=10 and quantity >= 5:
                    my_status ="bad"
        else:
                    my_status ="good" 
        


        # request.data['status'] = status
        new_dict = {**request.data, 'status': my_status}
        # request.data.update({"status":status})
        
        serializer = StockSerializer(data=new_dict)
        if serializer.is_valid():       
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
    def get(self, request, format=None):
        stocks = Stock.objects.select_related('book_id').all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

        


#-------------------------------------------------------------------------------------------------------------------------------

# GET SPECIFIC STOCK , UPDATING, DELETING SPECIFIC STOCK
class StockDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        stocks = self.get_object(pk)
        serializer =StockSerializer(stocks)
        return Response(serializer.data)

    

    def patch(self, request, pk, format=None):
        books = self.get_object(pk)
        serializer = StockSerializer(books, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        stocks = self.get_object(pk)
        stocks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#----------------------------------------------------------------------

# RETRIEVING STOCK HISTORY PER STOCK
class StockHistory(APIView):
    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        stocks = self.get_object(pk)
        serializer = StockSerializer(stocks)
        return Response(serializer.data)
