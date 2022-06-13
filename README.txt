Book Store Inventory Management System

1.Make sure you have python 3.6 installed
2.Install Django
3.Make sure your current folder is empty.
4.Create a new project
	$ django-admin startproject <project_name>
5.Install all the depenencies and get inside your recently created python envirnoment.
6.Run migrations
	$ python manage.py migrate
7.Start the python server
	$ python manage.py runserver

NOTE 
ACCESS TO THE VARIOUS ENDPOINTS
=to create an author

http://127.0.0.1:8000/store/create/



=to add Book and get all listing of books

http://127.0.0.1:8000/store/all/



=to update,get by id and delete book
http://127.0.0.1:8000/store/details/pk/




=To add stock and get all listing of stock

http://127.0.0.1:8000/store/stock/listing/




=To update, get by id and delete stock

http://127.0.0.1:8000/store/stock/details/pk/


