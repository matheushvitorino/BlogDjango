from django.urls import path
from . import views

app_name = 'blog'

urlpatterns=[
    path('home/', views.home, name="home"),
    path('postar/',views.postar, name="postar"),
    path('post/<int:id>/', views.post, name="post"),
]


