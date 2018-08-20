from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as sistemavotacao

app_name = 'sistemavotacao'

urlpatterns = [
	path('', sistemavotacao.Index.as_view(), name='home'),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('cadastro/', sistemavotacao.CriarUsuario.as_view(), name='cadastro'),
	path('adicionar-proposta/', sistemavotacao.AddProposta.as_view(), name='adicionar-proposta'),
	path('proposta/detalhes/<pk>', sistemavotacao.DetalhesProposta.as_view(), name='detalhes-proposta'),
]