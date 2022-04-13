
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import re_path
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from news.view import NewsView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # роутинг авторизации
    path('accounts/', include('accounts.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),

    # создание, получение, удаление новостей
    re_path('news/', NewsView.as_view(), name="News"),
] 
