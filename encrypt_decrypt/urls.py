from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cloud-home'),
    path('about/', views.about, name='cloud-about'),
    path('encrypt/', views.encrypt, name='cloud-encrypt'),
]