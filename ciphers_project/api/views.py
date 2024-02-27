from django.shortcuts import render
from django.http import JsonResponse
from .cipher import caesar_encode

def greetings(request):
    result = {"message": "Welcome to ciphers Service"}
    return JsonResponse(result)


def encode(request, plaintext, shift):
    cipher = caesar_encode(plaintext, shift)
    return JsonResponse({"cipher":cipher})
    
