from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid

class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, blank=True, related_name="uuiduser_set", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

class Proposta(models.Model):
	ususario = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, verbose_name='usuario', related_name='users')
	nome = models.CharField(max_length = 255, verbose_name = 'nome')
	descricao = models.TextField(verbose_name = 'descrição') 
	criado = models.DateTimeField(auto_now_add = True, verbose_name = 'criação')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'proposta'
		verbose_name_plural = 'propostas'

class Comentario(models.Model):
	usuario = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='user', verbose_name='usuário')
	proposta = models.ForeignKey(Proposta, on_delete=models.CASCADE, related_name='propostas', verbose_name='proposta')
	comentario = models.TextField(verbose_name='comentário')

	def __str__(self):
		return self.comentario

	class Meta:
		verbose_name = 'comentário'
		verbose_name_plural = 'comentários'