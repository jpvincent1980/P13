from django.contrib import admin
from django.urls import path, include

from lettings.views import index, letting
from profiles.views import profile, profiles_index
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profile, name='profile'),
    path('admin/', admin.site.urls),
]
