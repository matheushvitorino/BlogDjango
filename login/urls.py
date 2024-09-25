from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('registrar/', views.registrar, name="registrar"),
    path('ex_autenticado/', views.ex_autenticado, name='autenticado'), 
    path('logout/', views.logout, name="logout")  
]