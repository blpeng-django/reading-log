from operator import mod
from django.db import models
from rest_framework.serializers import ModelSerializer

# Create your models here.


class Book(models.Model):
    BID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'books'

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class User(models.Model):
    UID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'users'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class BookUser(models.Model):
    BID = models.ForeignKey('Book', on_delete=models.CASCADE)
    UID = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'bookuser'

class BookUserSerializer(ModelSerializer):
    class Meta:
        model = BookUser
        fields = "__all__"