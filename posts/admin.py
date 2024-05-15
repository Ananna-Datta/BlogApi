from django.contrib import admin
from .models import Post
# Register your models here.
from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','category']
    
    def first_name(self,obj):
        return obj.user.first_name
    
    def last_name(self,obj):
        return obj.user.last_name
    
    
admin.site.register(Post)
admin.site.register(models.Review)