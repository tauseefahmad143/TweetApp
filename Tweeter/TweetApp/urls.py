from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.tweet_list, name="tweet_list"),
    path('create/', views.tweet_create, name="tweet_create"),
    path('<int:tweet_id>/edit/', views.tweet_edit, name="tweet_edit"),
    path('<int:tweet_id>/delete/', views.tweet_delete, name="tweet_delete"),
    path('register/', views.register, name="register"),
    path('<int:tweet_id>/logout/', views.logout, name="logout"),
    path('search/', views.tweet_search, name='tweet_search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
