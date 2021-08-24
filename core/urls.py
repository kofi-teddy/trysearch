from django.contrib import admin
from django.urls import path
from apps.book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', views.post_search, name='post_search'),
]
