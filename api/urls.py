from django.urls import path
from .views import book, user

urlpatterns = [
    path('book/', book),
    path('user/', user)
]
