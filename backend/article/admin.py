from django.contrib import admin
from django.contrib.auth.models import Group
from .models import article_model


class changeList(admin.ModelAdmin):
    list_display = ('name','content')
    list_filter  = ('name','content')



# Register your models here.
#admin.site.unregister(Group)
admin.site.register(article_model, changeList)