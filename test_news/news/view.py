from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from requests import get

from .models import News
from .form import NewsForm

from comments.form import CommentsForm
from comments.models import Comments

import environ


class NewsView(TemplateView):
    template_name = 'tokens/create.html'
    
    def get(self, request, *args, **kwargs):
        
        # получение всех новостей и создание формы
        new_form = NewsForm()
        news = News.objects.all()
        
        # получение всех комментариев к статье и создание формы    
#        comment_form = CommentsForm()
#        comments = Comments.objects.filter(new = news)
        return render(request, 'news/get.html', {'form' : new_form, 'news' : news, 'comment_form' : comment_form, 'comments' : comments})


    def post(self, request):
        form = NewsForm(request.POST)
        form_empty = NewsForm()
        news = News.objects.all()
        
        if form.is_valid():
            
            # save params
            req = form.save(commit=False)
            req.save()
            
        return render(request, 'news/get.html', {'form' : form_empty, 'news' : news})
