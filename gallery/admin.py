from django.contrib import admin
from .models import Picture

# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    filter_horizontal = ('tag', )
    
    admin.site.register(Picture)