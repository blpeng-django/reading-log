from rest_framework.decorators import api_view
from api.models import Book, User, BookUser
from api.serializers import BookSerializer, UserSerializer, BookUserSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.


@api_view(["GET", "POST", "PUT", "DELETE"])
def user(request):
    if request.method == "GET":
        user = User.objects.all()
        serializedUser = UserSerializer(user, many=True)
        return JsonResponse({"data": serializedUser.data}, json_dumps_params={'ensure_ascii' : False})
    elif request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        user = User.objects.create(name=data["username"])
        serializedUser = UserSerializer(user)
        return JsonResponse({"data": serializedUser.data}, json_dumps_params={'ensure_ascii' : False})
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        User.objects.filter(name=data["before"]).update(name=data["after"])
        return JsonResponse({"data": True}, json_dumps_params={'ensure_ascii' : False})
    elif request.method == "DELETE":
        data = JSONParser().parse(request)
        User.objects.filter(name=data["username"]).delete()
        return JsonResponse({"data": True}, json_dumps_params={'ensure_ascii' : False})



@api_view(["GET", "POST", "PUT", "DELETE"])
def book(request):
    if request.method == "GET":
        data = JSONParser().parse(request)
        user = User.objects.get(name=data["username"])
        serializedUser = UserSerializer(user)
        bookuser = BookUser.objects.filter(UID=serializedUser.data["UID"])
        serializedBookUser = BookUserSerializer(bookuser, many=True)
        arr = []
        for data in serializedBookUser.data:
            book = Book.objects.get(BID=data["BID"])
            serializedBook = BookSerializer(book)
            arr.append(serializedBook.data)
        return JsonResponse({"data": arr}, json_dumps_params={'ensure_ascii' : False})
    elif request.method == "POST":
        data = JSONParser().parse(request)
        user = User.objects.get(name=data["username"])
        book = Book.objects.create(name=data["bookname"])
        BookUser.objects.create(UID=user, BID=book)
        return JsonResponse({"data": BookSerializer(book).data}, json_dumps_params={'ensure_ascii' : False})
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        Book.objects.filter(name=data["beforebookname"]).update(name=data["afterbookname"])
        return JsonResponse({"data": True}, json_dumps_params={'ensure_ascii' : False})
    elif request.method == "DELETE":
        data = JSONParser().parse(request)
        Book.objects.filter(name=data["bookname"]).delete()
        return JsonResponse({"data": True}, json_dumps_params={'ensure_ascii' : False})
