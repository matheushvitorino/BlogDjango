from django.urls import path
from . import views

urlpatterns=[
    path('home/', views.home, name="home"),
    path('postar/',views.postar, name="postar"),
    path('post/<int:id>/', views.post, name="post"),
]


