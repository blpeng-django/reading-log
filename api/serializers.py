from rest_framework.serializers import ModelSerializer
from api.models import Book, User, BookUser

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class BookUserSerializer(ModelSerializer):
    class Meta:
        model = BookUser
        fields = "__all__"