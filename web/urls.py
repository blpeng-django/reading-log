from django.urls import path
from .views import register, book, read

urlpatterns = [
    path('register/', register),
    path('book/', book),
    path('read', read)
]
