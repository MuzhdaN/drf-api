from django.contrib import admin
from .models import Profile

# register the profile so it shows up in admin panel
admin.site.register(Profile)
