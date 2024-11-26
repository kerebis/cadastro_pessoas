from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm

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

