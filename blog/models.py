from django.db import models
from django.urls import reverse

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    date = models.DateTimeField()
    post = models.TextField()
    #image = models.ImageField(null=True, blank=True, help_text="Optional: Upload a related image")

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

    def __str__(self):
        return self.title

# TODO: add image functionality to BlogPost model and integrate into webpages