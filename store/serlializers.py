from django.db.models import fields
from rest_framework import serializers
from store.models import Book, Author, Stock




class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields =('__all__')

class BookSerializer(serializers.ModelSerializer):
    #status = serializers.Field()
    
    
    class Meta:
            model = Book
            fields = ('title','author_id','YearOfPublication','description')


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        # status = serializers.ReadOnlyField()
        model = Stock
        fields =('book_id','quantity','status')