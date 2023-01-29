from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Book
from .serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
def home(request):
    return HttpResponse('Hi its Workingaaa............!!!')


# def booksList (request):
#     books = Book.objects.all()
#     booksPython = list(books.values())
#     return JsonResponse({
#          'books': booksPython
#         })
#          or you can use method given below


@api_view(['GET'])
def books_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


def samir(request):
    return HttpResponse("hiiii")


@api_view(['POST'])
def add_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['GET', 'PUT', "DELETE"])
def book(request, pk):
    try:
        book1 = Book.objects.get(pk=pk)
    except:
        return Response({
            "error":"Book Does Not Exist"
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BookSerializer(book1)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = BookSerializer(book1,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        """OR
        return Response({
            "delete": True)"""
