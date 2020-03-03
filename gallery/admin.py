from django.contrib import admin
from .models import Picture

# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    
    admin.site.register(Picture)