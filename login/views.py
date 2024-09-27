from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
    if request.user.is_authenticated:
        return  HttpResponse('ja esta autenticado')
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        usuario = request.POST.get('usuario')   
        senha = request.POST.get('senha')
        manter_conectado = request.POST.get('manter_conectado')
        autenticacao = authenticate(username = usuario, password = senha)
        
        if autenticacao:
            login_django(request, autenticacao)
            if manter_conectado:
                request.session.set_expiry(86400)
            else:
                request.session.set_expiry(0)
            
            return redirect('blog:home')
        else:
            messages.error(request, "Usuario ou senha incorretos.")
            return redirect('login:login')
        
    
def logout(request):
    if request.user.is_authenticated:
        logout_django(request)
        return redirect('login:login')
    else:
        return redirect('blog:home')
        
 
 #teste pra ser excluido depois    
@login_required(login_url="/login/login")       
def ex_autenticado(request):
    return HttpResponse('autenticado')  

