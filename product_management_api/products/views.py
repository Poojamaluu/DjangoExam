from django.shortcuts import render,get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from products.permissions import IsSuperUserOrReadOnly
from products.serializers import UserSerializer, ProductSerializer
from rest_framework import status
from products.models import Product
# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        serializer_instance=UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'messsage':'Logout Successfull'})


class ProductListCreate(APIView):
    permission_classes=[IsSuperUserOrReadOnly]
    def get(self,request):
        p=Product.objects.all()
        serializer_instance=ProductSerializer(p,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer_instance=ProductSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductRetrieveUpdateDelete(APIView):
    permission_classes=[IsSuperUserOrReadOnly]
    def get(self,request,id):
        p=get_object_or_404(Product,id=id)
        serializer_instance=ProductSerializer(p)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        p=get_object_or_404(Product,id=id)
        self.check_object_permissions(p,request)
        serializer_instance=ProductSerializer(instance=p,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        p=get_object_or_404(Product,id=id)
        self.check_object_permissions(p,request)
        p.delete()
        return Response({'message':'deleted successfully'},status=status.HTTP_204_NO_CONTENT)

