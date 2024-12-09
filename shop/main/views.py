from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello")


def calculator(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    return HttpResponse(f"Hello my name is {name}, I am {age} years old")


def post_data(request, name, age):
    return HttpResponse(f"Hello my name is {name}, I am {age} years old")


def calc(request, number1, char, number2):
    if char == '+':
        return HttpResponse(f"Result = {number1 + number2}")
    elif char == '-':
        return HttpResponse(f"Result = {number1 - number2}")
    elif char == '*':
        return HttpResponse(f"Result = {number1 * number2}")
    elif char == '%':
        try:
            return HttpResponse(f"Result = {number1 / number2}")
        except ZeroDivisionError:
            return HttpResponse("Zero division Error")
        

def calc_get(request):
    number1 = int(request.GET['number1'])
    char = request.GET['char']
    number2 = int(request.GET['number2'])
    if char == '+':
        return HttpResponse(f"Result = {number1 + number2}")
    elif char == '-':
        return HttpResponse(f"Result = {number1 - number2}")
    elif char == '*':
        return HttpResponse(f"Result = {number1 * number2}")
    elif char == '%':
        try:
            return HttpResponse(f"Result = {number1 / number2}")
        except ZeroDivisionError:
            return HttpResponse("Zero division Error")
        