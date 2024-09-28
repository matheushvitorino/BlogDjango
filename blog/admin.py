from django.contrib import admin
from .models import Post,Categoria,Tag,Comentario

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','resumo','conteudo','data','categoria')  # Exiba os campos que deseja na lista
    filter_horizontal = ('tag',)  # Permite selecionar múltiplas tags
    search_fields = ('titulo',)
    
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome','slug')
    search_fields = ('nome',)
    
class TagAdmin(admin.ModelAdmin):
    list_display = ('nome','slug')
    search_fields = ('nome',)
    
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('post_id','autor','conteudo','criado')
    search_fields = ('autor',)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Comentario, ComentarioAdmin)

