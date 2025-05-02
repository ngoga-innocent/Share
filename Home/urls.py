from django.urls import path
from .views import Home,AboutUs,ContactUs,BlogView,blog_detail_view,Event_View,Art
urlpatterns = [
   
    path('',Home,name='homepage'),
    path('about-us/',AboutUs,name='aboutus'),
    path('contact-us/', ContactUs.as_view(),name='contactus'),
    path('blog/', BlogView.as_view(),name='blog'),
    path('blogs/<slug:slug>/', blog_detail_view, name='blog_detail'),
    path('event',Event_View.as_view(),name='events'),
    path('event/<slug:slug>/',Event_View.as_view(),name='event'),
    path('arts',Art.as_view(),name='arts'),
   
    #path('ckeditor/', include('ckeditor_uploader.urls')),
]
