from django.db import models

# Create your models here.

class AboutUs(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.name
    
class SocialLink(models.Model):
    platform = models.CharField(max_length=20)
    link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.platform


    