from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

def registrar(request):
    if request.method == 'GET':
            return render(request,'registrar.html')
    else:    
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
    
        criar_usuario = User.objects.create_user(first_name=nome, last_name=sobrenome, username=usuario, email=email, password=senha)
        if criar_usuario:
            criar_usuario.save()
            return render(request,'login.html')
        else:
            render(request,'registrar.html')
            
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        autenticacao = authenticate(username = usuario, password = senha)
        if autenticacao:
            return HttpResponse('Login realizado')
        else:
            return HttpResponse('Erro')
 
 
 #teste pra ser escluido depois    
@login_required(login_url="/login/login")       
def ex_autenticado(request):
    return HttpResponse('autenticado')  

