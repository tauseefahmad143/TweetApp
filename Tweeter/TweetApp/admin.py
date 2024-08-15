from django.contrib import admin
from .models import Tweet
# Register your models here.
admin.site.register(Tweet)

class TweetAdmin(admin.ModelAdmin):
    list_display = ('username', 'text', 'created_at')
    search_fields = ('text', 'username')