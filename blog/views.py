from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from .models import Post,Categoria,Tag
from datetime import datetime,timezone

# Create your views here.
def home(request):
    #obtém todos posts
    posts = Post.objects.order_by('-data')

    
    # pega o primeiro post
    post_destaque = posts.first()
    
    # exclui o primeiro da fila, e pega os outros
    post_secundario = posts.exclude(id=post_destaque.id)[:2]
    

    
    post_inicial = posts[4]

    
    
    
    return render(
        request,'home.html',
        {'post_destaque':post_destaque,'post_secundario':post_secundario, 'posts':posts,'post_inicial':post_inicial})
    
    
def postar(request):
    categoria_tags = Categoria.objects.all()
    tag_box = Tag.objects.all()
    if request.method == 'POST':
        
        autor = 'Matheus'
        titulo = request.POST.get('titulo')      
        data = datetime.now()
        resumo = request.POST.get('resumo')
        conteudo = request.POST.get('conteudo')
        tag_id = request.POST.getlist('tag')#getlist chama por lista
        
        
        categoria_id = int(request.POST.get('categoria', 0))  
        categoria = get_object_or_404(Categoria,id=categoria_id)# Busca a categoria pelo ID 
        
        
        post = Post(autor=autor, titulo = titulo, resumo = resumo,  conteudo = conteudo, data = data, categoria = categoria)
        
        post.save() 

        
        if tag_id:
            for tag_id in tag_id:
                tag = get_object_or_404(Tag,id=tag_id)
                post.tag.add(tag)#O método add() é usado para adicionar uma ou mais instâncias ao campo ManyToManyField

        
        return redirect('postar')
        
    return render(request,'postar.html',{ 'categoria_tags': categoria_tags, 'tag_box': tag_box})


def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request,'post.html',{'post':post})
    
