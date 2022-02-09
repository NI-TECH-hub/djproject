from django.contrib import admin
# from . import models
from . models import TODO
# Register your models here.

# admin.site.register(models.TODO)

@admin.register(TODO)
class todoadmin(admin.ModelAdmin):
    list_display = ['id','title','deadline']
    
    