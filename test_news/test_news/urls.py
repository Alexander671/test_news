
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import re_path
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from news.view import NewsView, oneNewView
from .view import redirect_view


urlpatterns = [
    # создание, получение новостей
    # отдельной новости
    path('news/<int:pk>/', oneNewView.as_view(), name = 'OneNew'),
    path('news/', NewsView.as_view(), name = 'News'),
    path('',  NewsView.as_view(), name = 'News'),


    # роутинг авторизации
    path('accounts/', include('accounts.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),
    ]
                      