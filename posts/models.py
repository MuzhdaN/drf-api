from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.

    The auto_now_add parameter is set to True to automatically set 
    this field to the current date and time when the post is created.

    The auto_now parameter is set to True to automatically update 
    this field to the current date and time every time the post is
     saved.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_mlmkio', blank=True)
    image_filter_choices = [
        ('1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]

    class Meta:
        ordering = ['-created_at']
    
    """
    __str__ method is defined to return a string representation
     of the post, which consists of the post's ID and title.
    """
    def __str__(self):
        return f'{self.id} {self.title}'
