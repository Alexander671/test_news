from django.db import models
from news.models import News
class Comment(models.Model): # Таблица комментариев которая наследует models.Model
    
    # текст комментария
    category_text = models.TextField() # Текст комментария
    
    # родительский комментарий
    parent = models.ForeignKey('self',models.SET_NULL, unique=False, blank=True, null=True)
    
    # связь с новостью
    new = models.ForeignKey(News, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Category") # человекочитаемое имя объекта
        verbose_name_plural = ("Categories")  #человекочитаемое множественное имя для Комментариев
    def __str__(self):
        return self.category_text  # __str__ применяется для отображения объекта в интерфейсе