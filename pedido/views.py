from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class Pagar(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')

class FecharPedido(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('FecharPedido')

class Detalhe(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')


