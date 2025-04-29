from django.contrib import admin
from .models import Carousel,Blog,Mission
# Register your models here.
admin.site.register(Carousel)
# admin.site.register(Mission)

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display=('title',)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'slug','is_featured')
    prepopulated_fields = {'slug': ('title',)} 