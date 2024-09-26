from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect

def login_required_para_postar(view_func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'Você precisa estar logado para postar')
            return redirect('login')
        return view_func(request,*args,**kwargs)
    return wrapper