from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, "usuarios/home.html")

def usuarios(request):
    # Salvar usuário no BD
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get("nome")
    novo_usuario.idade = request.POST.get("idade")
    novo_usuario.save()
    # Exibir usuários
    usuarios = { "usuarios": Usuario.objects.all() }
    # Retornar dados para página de listagem
    return render(request, "usuarios/usuarios.html", usuarios)
