from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.
class Carousel(models.Model):
    image = models.ImageField(upload_to='carousel')
    
    def __str__(self):
        return self.image.name
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    category = models.CharField(max_length=100)
    date = models.DateField()
    description =  RichTextUploadingField()
    image = models.ImageField(upload_to='blog_images/')
    is_featured=models.BooleanField(default=False)
    tags = models.JSONField(default=list)

    def save(self, *args, **kwargs):
        # Automatically generate a slug from the title if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title     
class Mission(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextUploadingField()
    
    def __str__(self):
        return self.title
class Speaker(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='speakers',)
    bio=RichTextUploadingField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = RichTextUploadingField()
    thumbnail = models.ImageField(upload_to='events/')
    speakers = models.ManyToManyField(Speaker, related_name="events")
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while Event.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)
class EventSchedule(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    activity_name=models.TextField()
    start_time=models.TimeField(null=True,blank=True)
    end_time=models.TimeField(null=True,blank=True)
    description_title=models.TextField()
    description=RichTextUploadingField()
    location=models.TextField()
    
    def __str__(self):
        return self.activity_name
class Arts(models.Model):
    image=models.ImageField(upload_to='Arts/')
    name=models.CharField(max_length=255)
    description=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='Arts'
        ordering=['-created_at']
    
class Team(models.Model):
    profile=models.ImageField(upload_to='team_profile/')
    name=models.CharField(max_length=255)
    position=models.CharField(max_length=255)
    arrangement=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering=['arrangement',]
class OurImpact(models.Model):
    image = models.ImageField(upload_to='OurImpact/')
    name = models.CharField(max_length=255)
    
    slug = models.SlugField(unique=True, blank=True)
    story_title=models.CharField(max_length=255,null=True,blank=True)
    story = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            num = 1
            while OurImpact.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Our Impacts'
        ordering = ['-created_at']
    