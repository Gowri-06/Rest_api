from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . models import *
from rest_framework.parsers import JSONParser
from . serializers import ArticleSerializer
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication 
from rest_framework.permissions import IsAuthenticated
from django.views import View


def members(request):
    print("product")
    print(request)
    print(request.user)
    print("employ")

    return HttpResponse("Hello world!")


@csrf_exempt
def article(request):
    if request.method == "POST":
        print(request)
        # print(request.data)
        data = JSONParser().parse(request)
        print("data__check",data)
        serialzer = ArticleSerializer(data=data)
        print("serialzer",serialzer)
        if serialzer.is_valid():
           serialzer.save()
           return JsonResponse(serialzer.data,status = 201)
        return JsonResponse(serialzer.errors,status = 400)
    elif request.method == "GET":
            article_obj = Article.objects.all()
            serialzer = ArticleSerializer(article_obj,many=True)
            return JsonResponse(serialzer.data,safe=False) 

@csrf_exempt
def article_op(request,id):
    try:
        article_obj = Article.objects.get(id=id)
        print(article_obj)
    except Article.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer  = ArticleSerializer(article_obj)
        return JsonResponse(serializer.data)
    
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article_obj,data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        return JsonResponse(serializer.errors,status = 401)
    
    elif request.method == "DELETE":
        article_obj.delete()
        return HttpResponse("deleted",status=204)



@api_view(["GET","POST"])
def article_rest_api(request):
    if request.method == "POST":
        print(request)
        print(request.data)
        # data = JSONParser().parse(request)
        # print("data__check",data)
        serialzer = ArticleSerializer(data=request.data)
        print("serialzer",serialzer)
        if serialzer.is_valid():
           serialzer.save()
           return Response(serialzer.data,status=status.HTTP_201_CREATED)
        return Response(serialzer.errors,status = status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
            article_obj = Article.objects.all()
            serialzer = ArticleSerializer(article_obj,many=True)
            return Response(serialzer.data) 

@api_view(["GET","DELETE","PUT"])
def article_op_rest_api(request,id):
    print("checking reqqqqq",request)
    try:
        article_obj = Article.objects.get(id=id)
        print(article_obj)
    except Article.DoesNotExist:
        return Response("Error found",status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        
        # try:
            # article_obj = Article.objects.get(id=id)
            serializer  = ArticleSerializer(article_obj)
            print(article_obj)
            return Response(serializer.data)
            
        # except Article.DoesNotExist:
        #     return Response("DATA NOT",status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == "PUT":
        print(request.data)
        # data = JSONParser().parse(request)
        serializer = ArticleSerializer(article_obj,data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_401_UNAUTHORIZED)
    
    elif request.method == "DELETE":
        article_obj.delete()
        return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)


class ArticleApiView(APIView):
    #  authenticated_classes = [SessionAuthentication,BasicAuthentication]
     authenticated_classes = [TokenAuthentication]
     permission_classes = [IsAuthenticated]

     def get(self,request):
        ArticleObject = Article.objects.all()
        print(ArticleObject)
        serializer = ArticleSerializer(ArticleObject,many = True)
        return Response(serializer.data)
     def post(self,request):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     

class ArticleDetail(APIView):
    def get_obj(self,request,id):
        try:
            print("cccccc",request)
            return Article.objects.get(id=id)
            print('dddddd',article_obj)
        except Article.DoesNotExist:
            return Response("Error not found",status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,id):
        try:
            print("zzzzzzzzz",request)
            art_obj = self.get_obj(request,id)
            print("art_obj",art_obj)
            serializer = ArticleSerializer(art_obj)
            return Response(serializer.data)
        except:
            return Response("Id not found")

    def put(self,request,id):
        art_obj = self.get_obj(request,id)
        print(art_obj)
        serializer = ArticleSerializer(art_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        art_obj = self.get_obj(request,id)
        art_obj.delete()
        return Response("deleted",status=status.HTTP_204_NO_CONTENT)

class Task(View):
    def get(self,request,id):
        person  = Person.objects.get(id=id) 
        print(person.name)
        interest_of__person = person.interest.all()
        print(interest_of__person)
        for i in interest_of__person:
            print(i)
        return HttpResponse(interest_of__person)













        


     
     
     




        