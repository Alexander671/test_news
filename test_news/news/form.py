from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import News



class NewsForm(ModelForm):
    
    class Meta:
        model = News
        fields = ['name', 'new_text']