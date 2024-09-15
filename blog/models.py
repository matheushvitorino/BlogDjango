from django.db import models
from django.utils.text import slugify

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Verifica se o slug ainda não foi gerado
            self.slug = slugify(self.nome)  # Gera o slug a partir do nome
        super().save(*args, **kwargs)  # Chama o método save original para salvar o objeto

    def __str__(self):
        return self.nome
 
    
class Tag(models.Model):
    nome = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Verifica se o slug ainda não foi gerado
            self.slug = slugify(self.nome)  # Gera o slug a partir do nome
        super().save(*args, **kwargs)  # Chama o método save original para salvar o objeto

    def __str__(self):
        return self.nome
    

class Post(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100)
    resumo = models.CharField(max_length=150)
    conteudo = models.TextField()
    data = models.DateTimeField()
    categoria = models.ForeignKey(Categoria,on_delete=models.PROTECT, related_name='posts')
    tag = models.ManyToManyField(Tag,related_name='posts')
    
    def __str__(self):
        return f"{self.titulo} por {self.autor}"


    
