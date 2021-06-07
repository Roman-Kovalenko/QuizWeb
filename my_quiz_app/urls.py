from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questions_list/', views.questions_list, name='questions_list'),
    path('user_rating/', views.user_rating, name='user_rating')
]
