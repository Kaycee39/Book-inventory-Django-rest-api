
from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create_author.as_view(), name='create_author'),
    path('all/', views.view_books.as_view(), name = "create_book"),
    path('details/<int:pk>/', views.BookDetail.as_view(),name = "book_details"),
    path('stock/listing/',views.view_stock.as_view(), name ='create_stock'),
    path('stock/details/<int:pk>/',views.StockDetail.as_view(),name = "stock_details"),
    #path('stock/history/<int:pk>/',views.StockHistory.as_view()),
]
