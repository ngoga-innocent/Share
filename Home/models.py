from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
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