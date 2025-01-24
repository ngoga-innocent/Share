from django.shortcuts import render
from .models import Carousel,Blog,Mission
from django.views import View
from django.shortcuts import get_object_or_404
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
    context={
        'missions':missions
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
    