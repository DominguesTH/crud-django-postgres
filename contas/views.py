from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.shortcuts import render, redirect
from contas.models import Transacao
from .form import TransacaoForm



def nova_transacao(request):
  data = {}
  form = TransacaoForm(request.POST or None)

  if form.is_valid():
    form.save()
    return redirect('url_listagem')

  data['form'] = form
  return render(request, 'form.html', data)


def update(request, pk):
  data= dict()
  transacao = Transacao.objects.get(pk=pk)
  form = TransacaoForm(request.POST or None, instance=transacao)


  if form.is_valid():
    form.save()
    return redirect('url_listagem')

  data['form'] = form
  data['transacao'] = transacao
  return render(request, 'form.html', data)


def delete(request, pk):
  transacao = Transacao.objects.get(pk=pk)
  transacao.delete()
  return redirect('url_listagem')


def listagem(request):
  data = {}
  data['transacoes'] = Transacao.objects.all()
  return render(request, 'listagem.html', data)