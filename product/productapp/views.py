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
from rest_framework import generics 
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404 


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
    #  authenticated_classes = [TokenAuthentication]
    #  permission_classes = [IsAuthenticated]

     def got(self,request):
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
        print(person)
        print("name",person.name)
        interest_of_person = person.interest.all()
        print("interest_of_person",interest_of_person)
        address = person.personaddress
        print("address",address)
        print("address",address.city)
        print("address",address.person)
        print("address",address.street_address)
        for i in interest_of_person:
            print("i>>>",i)
        city = City.objects.get(id=id) 
        print(city)
        city_persons = city.personaddress_set.all() 
        print("city_persons",city_persons) 
        for j in city_persons:
            print("j>>>",j.person) 
            print("j>>>",j.street_address) 
            print("j>>>",j.city) 
        interest = Interest.objects.get(id=id)
        print(interest)
        interest_similar = interest.person_set.all()
        print("interest_similar",interest_similar)
        main_list = []
        for k in interest_similar:
            print("interest_similar",k.name)
            print("interest_similar",k.mobile)
            print("interest_similar",k.interest.all())
            b =  [d for d in k.interest.all()]
            print("b",b)
            c = [ k.name]
            f = [k.mobile]
            print("f",f)
            print("c",c)
            e = c + f + b
            print("eeeeeeeee",e)
            main_list.append(e)
        print("main_list",main_list) 
        return HttpResponse("success")

# class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin,mixins.CreateModelMixin,
#                      mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
#     print("hhhhh")
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
#     # lookup_field = "id"
#     def get(self,request,pk):
#         if pk:
#             return self.retrieve(request,pk) 
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
#     def put(self,request,pk):
#         return self.update(request,pk)
#     def delete(self,request,pk):
#         return self.destroy(request,pk)
    
# class ArticleViewSet(viewsets.ViewSet):
#     def list(self,request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#         return Response(serializer.data)
#     def create(self,request):
#         print("&&&&&&",request.data)
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def retrieve(self,request,pk=None):
#         print("retrieve method")
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset,pk=pk)
#         print(article.title)
#         print(article.author)
#         print(article.email)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data) 
#     def update(self,request,pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset,pk=pk)
#         print("llllllllllllll",article)
#         serializer = ArticleSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.save())
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def destroy(self,request,pk=None):
#         # article = Article.objects.get(id=pk)
#         # article.delete()
#         queryset = Article.objects.all()
#         article1 = get_object_or_404(queryset,pk=pk)
#         print(article1)
#         article1.delete()
#         return Response("DELETED")

# class ArticleTwoViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
#                         mixins.DestroyModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


class ArticleThreeViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer







        
























        


     
     
     




        