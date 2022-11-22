from django.shortcuts import render
from .forms import SignUpForm, SignInForm
from .serializers import RegisterSerializer, LoginSerializer, CarSerializer, PriceSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Register, LogIn_Wrong, CarDetails, CarPrice
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
@api_view(["POST", "GET"])
def signup(request):
    if request.method == "POST":
        # print(request.data)
        serializer = RegisterSerializer(data = request.data)
        form = SignUpForm(request.POST)
        if form.is_valid():
            serializer.is_valid(raise_exception = True)
            serializer.save()
            print("form",form)
            user = form.save()
            user.refresh_from_db()
            user.save()
        else:
            serializer.is_valid(raise_exception = True)
            serializer.save()
        return HttpResponse("User Register Successfully")
    
    elif request.method == "GET":
        print("GET")
        data = Register.objects.all()
        serializer = RegisterSerializer(data, many = True)
        print(serializer.data)
        return HttpResponse(serializer.data)

    else:
        return HttpResponse("Something is wrong")

@api_view(["POST", "GET"])
def signin(request):
    if request.method == "POST":
        data = request.data
        serializer = LoginSerializer(data = request.data)
        form = SignInForm(request.POST)
        check = Register.objects.filter(email = data["email"], password = data["password"])
        if form.is_valid() and check.exists():
            print("form",form)
            # user = form.save()
            # user.refresh_from_db()
            # user.save()
            return HttpResponse("Login Successfully")
        elif check.exists():
            return HttpResponse("Login Successfully")
        else:
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return HttpResponse("Please enter valid ID & Password")
    else:
        return HttpResponse("Welcome to Login Page")

@api_view(["POST", "GET"])
def viewcar(request):
    if request.method == "GET":
        data = CarDetails.objects.all()
        print(data.values())
        serializer = CarSerializer(data, many = True)
        return Response({"status":"Success", "data": serializer.data}, status = status.HTTP_200_OK)
    
    elif request.method == "POST":
        print("Start")
        filters = request.data["car_name"]
        # import pdb; pdb.set_trace()
        data = CarDetails.objects.filter(car_name = filters)

        if data.exists():
            serializer = CarSerializer(data, many = True)
            return Response({"status":"Success", "Data": serializer.data}, status = status.HTTP_200_OK)
        else:
            return HttpResponse("No such record exits for the car {}".format(filter))
        
@api_view(["POST"])
def addcar(request):
    if request.method == "POST":
        data = request.data
        print(data)
        serializer = CarSerializer(data = data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({"status":"Success", "Data": serializer.data}, status = status.HTTP_200_OK)

    else:
        return HttpResponse("Bad Request")

@api_view(["GET"])
def price(request, car = None):
    if request.method == "GET" and car:
        # import pdb; pdb.set_trace()c
        data = CarPrice.objects.filter(car_details_id = car)
        print(data.values())
        serializer = PriceSerializer(data, many = True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == "GET":
        data = CarPrice.objects.all()
        print(data.values())
        # import pdb; pdb.set_trace()
        serializer = PriceSerializer(data, many = True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    else:
        return HttpResponse("Bad Request")

@api_view(["POST"])
def prices(request):
    if request.method == "POST":
        data = request.data
        # print(data)
        serializer = PriceSerializer(data = data)

        if serializer.is_valid():

            # serializer.is_valid(raise_exception = True)
            # print(serializer.data)
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    else:
        return HttpResponse("Bad Request")


# @api_view(["GET"])
# def all(request):
#     if request.method == "GET":
#         data = CarPrice.objects.all()
#         print(data.car_name.all())
#         return Response(data.values())