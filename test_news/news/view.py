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


class oneNewView(TemplateView):
    # получение всех новостей 
    def get(self, request, pk, *args, **kwargs):
        new = News.objects.get(id = pk)

        # получение всех комментариев к статье и создание формы    
        comment_form = CommentsForm()
        comments = Comments.objects.filter(new = pk)
        print(comments)
        return render(request, 'news/get1.html', {'new' : new, 'comment_form' : comment_form, 'comments' : comments})
    def post(self, request, pk, *args, **kwargs):
        form_comment = CommentsForm(request.POST)
        form_empty = CommentsForm()
        new = News.objects.get(id = pk)
        comments = Comments.objects.filter(new = new)

        if form_comment.is_valid():
            
            # save params
            req = form_comment.save(commit=False)
            req.comment_autor = request.user
            req.new           = new
            req.save()
            
        return render(request, 'news/get.html', {'new' : new, 'comment_form' : form_empty, 'comments' : comments})



class NewsView(TemplateView):
    template_name = 'tokens/create.html'
    
    def get(self, request, *args, **kwargs):
        
        # получение всех новостей и создание формы
        new_form = NewsForm()
        news = News.objects.all()
        
        return render(request, 'news/get.html', {'form' : new_form, 'news' : news})


    def post(self, request):
        form = NewsForm(request.POST)
        form_empty = NewsForm()
        news = News.objects.all()
        
        if form.is_valid():
            
            # save params
            req = form.save(commit=False)
            req.save()
            
        return render(request, 'news/get.html', {'form' : form_empty, 'news' : news})

