from django.shortcuts import render
from .models import *
# Create your views here.
def Index (request):
    alunos = Aluno.objects.all()
    contexto = {
        'lista': alunos,
    }
    return render(request, 'estudante/index.html',contexto)