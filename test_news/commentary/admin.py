from django.contrib import admin
from .models import Comments
from mptt.admin import MPTTModelAdmin

admin.site.register(Comments, MPTTModelAdmin)
