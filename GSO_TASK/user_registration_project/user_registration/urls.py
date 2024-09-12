from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_user, name='register_user'),
    path('success/', views.registration_success, name='registration_success'),

]
