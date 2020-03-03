from django.contrib import admin
from .models import Picture, tags

# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
      
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)