from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from commentary.models import Comments

admin.site.register(Comments , MPTTModelAdmin) 