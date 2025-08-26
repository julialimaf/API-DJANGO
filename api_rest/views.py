from django.shortcuts import render

from django.http import HttpResponse , JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status

from .models import User 
from .serializers import UserSerializer 


import json 


@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
        
    return Response(status=status.HTTP_400_BAD_REQUEST) 


@api_view(['POST, GET','DELETE', 'PUT'])
def user_manager(request):
    if request.method == 'GET':
        user_nickname = request.GET.get('user', None)  

        if user_nickname:       
           
            try:
                user = User.objects.get(pk=user_nickname)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        
from django.shortcuts import render

@api_view(['POST'])
def cadastro(request):
    return render(request, 'cadastro.html')  # seu template de cadastro





# def databaseEmDjango(request):
#    data = User.objects.all(pk=)

   # data = User.objects.exclude()

   # data = User.objects.filter()

#    data.save()

   # data.delete()








