from django.shortcuts import render
from .models import Carousel,Blog,Mission,Event,Arts,Team
from django.views import View
from django.shortcuts import get_object_or_404
from django.utils import timezone

# Create your views here.
def Home(request):
    carousel = Carousel.objects.all()
    blogs = Blog.objects.all().order_by('-date')[:5]
    featured_blog = blogs[0] if blogs else None
    other_blogs = blogs[1:] if blogs else []
    context={
        'carousels': carousel,
        'featured_blog': featured_blog,
        'other_blogs': other_blogs,
    }
    return render(request, 'home.html',context)
def AboutUs(request):
    missions=Mission.objects.all()
    teams=Team.objects.all()
    context={
        'missions':missions,
        'teams':teams
    }
    return render(request,'aboutus.html',context)
class ContactUs(View):
    def get(self, request):
        return render(request, 'contact_us.html')
class BlogView(View):
    def get(self, request):
        blogs = Blog.objects.all().order_by('-date')
        featured_blogs=Blog.objects.filter(is_featured=True)
        return render(request, 'blog.html', {'blogs': blogs,"featured": featured_blogs})
def blog_detail_view(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog})   
class Event_View(View):
    def get(self,request,slug=None):
        now = timezone.now()
        if slug is not None:
            event = get_object_or_404(Event, slug=slug)
            schedules = event.eventschedule_set.order_by('start_time')
            speakers = event.speakers.all()
            return render(request, 'events/event_detail.html', {
                'event': event,
                'schedules': schedules,
                'speakers': speakers,
            })
        # Upcoming: date is in the future
        upcoming_events = Event.objects.filter(date__gte=now).order_by('date')

        # Past: date is in the past
        past_events = Event.objects.filter(date__lt=now).order_by('-date')
        return render(request,'event.html',{
            'upcoming_events':upcoming_events,
            'past_events':past_events
        })
class Art(View):
    def get(self,request,slug=None):
        featured_arts=Arts.objects.all()[:5]
        all_arts=Arts.objects.all()
        return render(request,'art.html',{
            'featured_arts':featured_arts,
            'all_arts':all_arts
        })
    