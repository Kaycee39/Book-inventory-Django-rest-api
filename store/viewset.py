from rest_framework.decorators import APIView
from rest_framework.response import Response
from store.models import Book, Author
from store.serlializers import BookSerializer,AuthorSerializer

@APIView(['GET'])
def InventoryOverview(request):
    store_urls={
        'all_books' : '/',
        'search by year of publication':'/?yearofpublication = category_name',
        'search by author' : '/?author = category_name',
        'add':'/create',
        'update':'/update/pk',
        'delete':'/book/pk/delete', 
    }
    return Response(store_urls)

