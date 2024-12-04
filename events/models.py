from django.db import models
from django.contrib.auth.models import User

PERMITTED = ((0, "Yes"), (1, "No"))
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_posts")
    category = models.CharField(max_length=200)
    # event_image = CloudinaryField('image', default='placeholder')
    date = models.DateTimeField()
    time = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    familiar = models.IntegerField(choices=PERMITTED, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)