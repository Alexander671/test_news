from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class News(models.Model): # Таблица новостей которая наследует models.Model
    name = models.CharField(max_length=100) # название новости
    new_text = models.TextField(blank=False) # текст новости 
    date_of_create = models.DateField(auto_now_add=True) # дата создания
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank = True, null = True)
    class Meta:
        verbose_name = ("New") # человекочитаемое имя объекта
        verbose_name_plural = ("News")  #человекочитаемое множественное имя для Категорий
    def __str__(self):
        return self.name  # __str__ применяется для отображения объекта в интерфейсе
