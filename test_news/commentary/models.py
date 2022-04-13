from django.conf import settings
from django.db import models
from news.models import News
from mptt.models import MPTTModel, TreeForeignKey
class Comments(models.Model): # Таблица комментариев которая наследует models.Model
    
    # текст комментария
    comment_text = models.TextField() # Текст комментария
    
    # родительский комментарий
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    # связь с новостью
    new = models.ForeignKey(News, on_delete=models.CASCADE)

    # автор комментария
    comment_autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank = True, null = True)

    
    class Meta:
        verbose_name = ("Category") # человекочитаемое имя объекта
        verbose_name_plural = ("Categories")  #человекочитаемое множественное имя для Комментариев
    def __str__(self):
<<<<<<< HEAD:test_news/commentary/models.py
        return self.comment_text  # __str__ применяется для отображения объекта в интерфейсе

    class MPTTMeta:
         order_insertion_by = ['comment_text']
||||||| fd5c6b0:test_news/comments/models.py
        return self.comment_text  # __str__ применяется для отображения объекта в интерфейсе
=======
        return self.comment_text  # __str__ применяется для отображения объекта в интерфейсе
>>>>>>> 5dcb18161bcf619c669215bd5281e573a1a0c122:test_news/comments/models.py
