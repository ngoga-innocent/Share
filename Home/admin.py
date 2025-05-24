from django.contrib import admin
from .models import Carousel,Blog,Mission,Speaker,Event,EventSchedule,Arts,Team,OurImpact
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
class EventScheduleInline(admin.StackedInline):  # or use StackedInline for vertical layout
    model = EventSchedule
    extra = 1  # How many empty forms to show
class EventAdmin(admin.ModelAdmin):
    inlines = [EventScheduleInline]
    list_display = ['title', 'date', 'created_at']
    prepopulated_fields = {"slug": ("title",)}  # Optional: auto-generate slug
    filter_horizontal = ('speakers',)  # Adds a UI to pick multiple speakers
admin.site.register(Event, EventAdmin)
admin.site.register(Speaker)
admin.site.register(Arts)
admin.site.register(Team)
admin.site.register(OurImpact)