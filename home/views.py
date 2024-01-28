from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import nameserializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication , SessionAuthentication , TokenAuthentication
from home.custom_authroization import CustomAuthentication
from rest_framework.permissions import IsAuthenticated , IsAdminUser , IsAuthenticatedOrReadOnly , DjangoModelPermissionsOrAnonReadOnly
# from .custom_permisiions import Mypermission
from rest_framework_simplejwt.authentication import JWTAuthentication

class studentViewSet(viewsets.ModelViewSet):
    
    queryset = name.objects.all()
    serializer_class = nameserializer
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication]
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [JWTAuthentication]
    
    permission_classes = [IsAuthenticated]
    # permission_classes =[IsAdminUser]
    # permission_classes =[IsAuthenticatedOrReadOnly]
    # permission_classes =[DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes =[Mypermission]
 
    

# manual define class and method 
# class studentViewSet(viewsets.ViewSet):
#     def list(self , request):
#         stu = name.objects.all()
#         serializer = nameserializer(stu , many = True)
#         return Response(serializer.data) 
    
#     def retrieve(self , request , pk= None):
#         id = pk
#         if id is not None:
#             stu = name.objects.get(id = id)
#             serializer = nameserializer(stu)
#             return Response(serializer.data)
        
#     def create(self , request):
#         serializer = nameserializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response( {"msg":'Data Created '},status = status.HTTP_201_CREATED )       
#         return Response( serializer.errors,status = status.HTTP_400_BAD_REQUEST)   
    
#     def update(self , request , pk):
#         id = pk
#         stu = name.objects.get(pk = id)
#         serializer = nameserializer(stu , data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response( {"msg":'Complete Data Update'},status = status.HTTP_201_CREATED ) 
#         return Response( serializer.errors,status = status.HTTP_400_BAD_REQUEST)  
    
#     def destroy(self , request , pk ):
        
#         id = pk
#         stu = name.objects.get(id= id)
#         stu.delete()
#         return Response({'msg':'data succesfully delete'})
         
        
                      
            