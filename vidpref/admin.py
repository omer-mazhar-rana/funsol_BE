from django.contrib import admin

from .models import User, Preferences, Video

admin.site.register(User)
admin.site.register(Preferences)
admin.site.register(Video)
