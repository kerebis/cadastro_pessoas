from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa
from .forms import PessoaForm

def pagina_inicial(request):
    return render(request, 'pessoas/pagina_inicial.html')

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas/listar_pessoas.html', {'pessoas': pessoas})

def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'pessoas/cadastrar_pessoa.html', {'form': form})

def editar_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'pessoas/editar_pessoa.html', {'form': form, 'pessoa': pessoa})

def deletar_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('listar_pessoas')
    return render(request, 'pessoas/deletar_pessoa.html', {'pessoa': pessoa})