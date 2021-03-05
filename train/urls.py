
from django.urls import path, include
from . import views


urlpatterns = [
    path("",views.index, name="train"),
    path("booking/<book>", views.booking, name='booking'),
    path("booksub", views.booksub, name='booksub'),

]