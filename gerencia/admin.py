from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

@admin.register(Aluno)
class AlunoAdmin (admin.ModelAdmin):
    def imagem_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    imagem_tag.short_description = 'imagem'
    list_display =['nome','email', 'data_nacimento', 'imagem']