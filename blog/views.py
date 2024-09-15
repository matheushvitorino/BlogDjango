from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def home(request):
    #obtém todos posts
    posts = Post.objects.order_by('-data')
    
    # pega o primeiro post
    post_destaque = posts.first()
    
    # exclui o primeiro da fila, e pega os outros
    post_secundario = posts.exclude(id=post_destaque.id)[:3]
    
    return render(
        request,'home.html',
        {'post_destaque':post_destaque,'post_secundario':post_secundario })
