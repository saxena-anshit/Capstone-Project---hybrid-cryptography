from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='cloud-home'),
    path('encrypt/', views.encrypt, name='cloud-encrypt'),
    path('decrypt/', views.decrypt, name='cloud-decrypt'),
]