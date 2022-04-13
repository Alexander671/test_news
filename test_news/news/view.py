from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from requests import get
from .models import News
from .form import NewsForm

import environ


class NewsView(TemplateView):
    template_name = 'tokens/create.html'
    
    def get(self, request, *args, **kwargs):
        form = NewsForm()
        news = News.objects.all()
        return render(request, 'news/get.html', {'form' : form, 'news' : news})


    def post(self, request):
        form = NewsForm(request.POST)
        form_empty = NewsForm()
        news = News.objects.all()
        
        if form.is_valid():
            
            # save params
            req = form.save(commit=False)
            req.save()
            
        return render(request, 'news/get.html', {'form' : form_empty, 'news' : news})
