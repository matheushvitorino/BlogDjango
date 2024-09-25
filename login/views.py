from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
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
            
            return HttpResponse('Login realizado')
        else:
            return HttpResponse('Erro')
        
@login_required(login_url="/login/login")
def logout(request):
    logout_django(request)
    return render(request,'login.html')
        
 
 #teste pra ser excluido depois    
@login_required(login_url="/login/login")       
def ex_autenticado(request):
    return HttpResponse('autenticado')  

