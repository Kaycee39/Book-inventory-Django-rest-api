
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('create/',views.create_author.as_view()),
    path('all/', views.view_books.as_view()),
    path('details/<int:pk>/', views.BookDetail.as_view()),
    path('stock/listing/',views.view_stock.as_view()),
    path('stock/details/<int:pk>/',views.StockDetail.as_view()),
]
