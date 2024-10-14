from django.urls import path
from . import views

urlpatterns = [
    path('helloWorld/', views.hello_world_view),
    path('list/', views.get_books),
    path('addBook/', views.add_book)
]