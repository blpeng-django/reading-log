from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests

# Create your views here.
@csrf_exempt
def register(request):
    if request.method == "GET":
        return HttpResponse(
        """
        <form method="POST">
            <input type="text" name="text">
            <input type="submit" value="가입">
        </form>
        """
        )
    elif request.method == "POST":
        name = request.POST.get("text")
        data = {
            "username": name
        }
        response = requests.post("http://127.0.0.1:8000/api/user/", json=data)
        return HttpResponse(response)
@csrf_exempt
def read(request):
    if request.method == "GET":
        return HttpResponse(
        """
        <form method="POST">
            <input type="text" name="user", title="유저이름">
            <input type="submit" value="조회">
        </form>
        """
        )
    elif request.method == "POST":
        user = request.POST.get("user")
        data = {
            "username": user
        }
        response = requests.get("http://127.0.0.1:8000/api/book/", json=data)
        return HttpResponse(response)
@csrf_exempt
def book(request):
    if request.method == "GET":
        return HttpResponse(
        """
        <form method="POST">
            <input type="text" name="user", title="유저이름">
            <input type="text" name="book", title="책이름">
            <input type="submit" value="등록">
        </form>
        """
        )
    elif request.method == "POST":
        user = request.POST.get("user")
        book = request.POST.get("book")
        data = {
            "username": user,
            "bookname": book
        }
        response = requests.post("http://127.0.0.1:8000/api/book/", json=data)
        return HttpResponse(response)