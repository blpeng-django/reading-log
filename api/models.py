from django.db import models


class Book(models.Model):
    BID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'books'



class User(models.Model):
    UID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'users'



class BookUser(models.Model):
    BID = models.ForeignKey('Book', on_delete=models.CASCADE)
    UID = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'bookuser'
