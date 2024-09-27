from django.urls import path
from . import views


urlpatterns =[
    path('post/<int:id>/comentarios/', views.comentarios.as_view(), name="comentarios"),
]