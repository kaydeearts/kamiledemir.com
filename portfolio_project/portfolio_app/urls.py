from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='profiles'),
    # path('', views.profile_get, name='profile_get')
]
