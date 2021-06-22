from django import forms
from django.forms import ModelForm
from appPeludo.models import Mascotas

class MascotasForm(ModelForm):
	class Meta:
		model = Mascotas
		fields = ['id','anios','nombre','especie','vacunado','codigo']