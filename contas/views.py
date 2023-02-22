from django.shortcuts import render
from .models import Transacao

# Create your views here.

def home(request):
    data = {}
    return render(request, 'contas/home.html', data)


def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()

    return render(request, 'contas/listagem.html', data)
