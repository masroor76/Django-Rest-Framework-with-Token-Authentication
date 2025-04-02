from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import *


class LoginView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({
                "status":401,
                "data":serializer.errors
            })
        username = request.data['username']
        password = request.data['password']
        print(username,password)
        user_obj = authenticate(request, username = username, password = password)
        if user_obj:
            token , _ = Token.objects.get_or_create(user = user_obj)
            return Response({
                "status":True,
                "data": {'token': str(token)}
            })
        return Response({
            'status': False,
            'data':{} ,
            'message': "Invalid credentials!"
        }) 



class RegisterView(APIView):
    def post(self, request, format=None): 
        username = request.data['username']
        password = request.data['password']
        password2 = request.data['password2']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        if password == password2:
            user_data = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user_data.save()
            return Response("User Created",  status= 201)
        else:
            raise("Recheck your Password")
        