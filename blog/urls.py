from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index),
    path('home/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('new_post/', views.new_post),
    path('<int:pk>/', views.single),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]