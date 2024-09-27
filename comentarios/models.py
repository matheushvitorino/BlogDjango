from django.db import models
from blog.models import Post
from django.contrib.auth.models import User

class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    post =  models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    comentariopostado = models.TextField()
    criado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.autor.username} - {self.comentario[:30]}'