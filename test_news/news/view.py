from pipes import Template
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from requests import get

from .models import News
from .form import NewsForm

from commentary.form import CommentsForm
from commentary.models import Comments

import environ

from mptt.forms import MoveNodeForm
class oneNewView(TemplateView):
    # получение всех новостей 
    def get(self, request, pk, *args, **kwargs):
        new = News.objects.get(id = pk)

        # получение всех комментариев к статье и создание формы    
        form_comment = CommentsForm()
        comments = Comments.objects.filter(new = new)
        return render(request, 'news/get1.html', {'new' : new, 'comment_form' : form_comment, 'comments' : comments})
    
    def post(self, request, pk, *args, **kwargs):

        # форма которую мы получили 
        form_comment = CommentsForm(request.POST)
        
        # очистка формы
        form_empty = CommentsForm()
        
        # поиск новостей по id
        new = News.objects.get(id = pk)
        
        # комментарии которые относятся к этой статье
        comments = Comments.objects.filter(new = new)

        if form_comment.is_valid():
            
            # save params
            req = form_comment.save(commit=False)
            req.comment_autor = request.user
            req.new           = new
            req.save()
            
        return render(request, 'news/get1.html', {'new' : new, 'comment_form' : form_empty, 'comments' : comments})



class NewsView(TemplateView):
    template_name = 'tokens/create.html'
    
    def get(self, request, *args, **kwargs):
        
        # получение всех новостей и создание формы
        form_new = NewsForm()
        news = News.objects.all()
        
        return render(request, 'news/get.html', {'form' : form_new, 'news' : news})


    def post(self, request):
        
        # форма которую мы получили 
        form = NewsForm(request.POST)

        # отчистка формы
        form_empty = NewsForm()

        # все новости
        news = News.objects.all()
        
        if form.is_valid():
            
            # save params
            req = form.save(commit=False)
            req.autor         = request.user
            req.save()
            
        return render(request, 'news/get.html', {'form' : form_empty, 'news' : news})

