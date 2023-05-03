"""product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from productapp import views 
from . import views 
from .views import ArticleApiView, ArticleDetail, Task, ArticleThreeViewSet
# ArticleViewSet,GenericAPIView,ArticleTwoViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register('article',ArticleViewSet,basename='article')
# router.register('articletwo',ArticleTwoViewSet,basename='articletwo')
router.register('articlethree',ArticleThreeViewSet,basename='articlethree')

urlpatterns = [
    path('viewsetthree/',include(router.urls)),
    path('viewsetthree/<int:pk>/',include(router.urls)),
    path('viewsettwo/',include(router.urls)),
    path('viewsettwo/<int:pk>/',include(router.urls)),
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    # path('admin/', admin.site.urls),
    path('hello/',views.members,name="members"),
    # path('article/',views.article, name="article"),
    # path('article_op/<int:id>/',views.article_op, name="article_op"),
    path('article_rest_api/',views.article_rest_api, name="article_rest_api"),
    path('article_op_rest_api/<int:id>/',views.article_op_rest_api, name="article_op_rest_api"),
    path('article_api_view/',ArticleApiView.as_view(), name="articleapiview"),
    path('article_detail/<int:id>/',ArticleDetail.as_view(), name="articledetail"),
    path('task/<int:id>/',Task.as_view(), name="task"),
    # path('generic/article/<int:pk>/',GenericAPIView.as_view(),name="genericapi"),
    # path('secondgeneric/article/<int:pk>/',GenericAPIView.as_view(),name="secondgenericapi"),

]
