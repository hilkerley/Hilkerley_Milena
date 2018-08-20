from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import *
from .forms import *

class Index(ListView):
	model = Proposta
	template_name = 'index.html'

class DetalhesProposta(DetailView):
	model = Proposta
	template_name = 'proposta.html'

class CriarUsuario(CreateView):
    model = UUIDUser
    template_name = 'cadastrar.html'
    success_url = reverse_lazy('sistemavotacao:home')
    form_class = AdicionarUsuario

    def form_valid(self, form):
    	obj = form.save(commit=False)
    	obj.set_password(obj.password)
    	obj.save()
    	return super(CriarUsuario, self).form_valid(form)

class AddProposta(CreateView):
	model = Proposta
	template_name = 'adicionar.html'
	success_url = reverse_lazy('sistemavotacao:home')
	form_class = Cadastrar

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.save()
		return super(AddProposta, self).form_valid(form)


