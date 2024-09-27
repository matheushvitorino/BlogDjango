from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from .models import Comentario
from blog.models import Post
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class comentarios(LoginRequiredMixin,CreateView):
    model = Comentario
    fields = ["comentariopostado","criado"] 
    template_name = "post.html"
    
    def form_valid(self,form):
        post_id = self.kwargs['id']
        post = get_object_or_404(Post, id=post_id)
        comentario = form.save(commit=False)
        comentario.post = post
        comentario.autor = self.request.user
        return super().form_valid(form)
        
    
    def get_success_url(self):
        postid = self.object.post.id
        
        return reverse_lazy('post', kwargs={'id': postid})
