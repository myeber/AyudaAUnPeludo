from appPeludo.forms import MascotasForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from appPeludo.models import Mascotas

def home(request):
	return render(request, 'index.html')

def perros(request):
	return render(request, 'perros.html')

def gatos(request):
	return render(request, 'gatos.html')

def acercade(request):
	return render(request, 'acercade.html')

def cookie(request):
	return render(request, 'cookie.html')

def daisy(request):
	return render(request, 'daisy.html')

def kota(request):
	return render(request, 'kota.html')

def arbor(request):
	return render(request, 'arbor.html')

def blizzard(request):
	return render(request, 'blizzard.html')

def bob(request):
	return render(request, 'bob.html')

def listar_mascotas(request):
	mascotas = Mascotas.objects.all()

	return render(request, 'listamascotas.html', {'mascotas':mascotas})

def crearMascota(request):
	mascota = Mascotas(
	codigo = "MAS006",
	anios = "4",
	nombre = "Bob",
	especie = "Felino",
	vacunado = True
	)
	mascota.save()

	return HttpResponse("Registro mascota creado.")

def crearMascotaNav(request, codigo, anios, nombre, especie, vacunado):
	mascota = Mascotas(
	codigo = codigo,
	anios = anios,
	nombre = nombre,
	especie = especie,
	vacunado = vacunado
	)
	mascota.save()

	return redirect('listarMascotas')

def leer_mascota(request, id):
	mascota = Mascotas.objects.get(id=id)

	return HttpResponse(f"La mascota es: {mascota.codigo}, {mascota.nombre}")

def editar_mascota(request, id):
	mascota = Mascotas.objects.get(id=id)

	mascota.nombre = "Pecca"

	mascota.save()

	return HttpResponse(f"Nombre de la mascota actualizado: {mascota.nombre}")

def borrar_mascota(request, id):
	mascota = Mascotas.objects.get(id=id)

	mascota.delete()

	return redirect('listarMascotas')

def nuevaMascota(request):
	return render(request, 'nuevaMascota.html')

def guardarMascota(request):
	codigo = request.POST['codigo']
	nombre = request.POST['nombre']

	mascota = Mascotas(
		codigo = codigo,
		anios = "",
		nombre = nombre,
		especie = "",
		vacunado = 0
	)

	mascota.save()

	return redirect('listarMascotas')

def formMascota(request):
	datos = {
		'form' : MascotasForm()
	}
	if request.method == 'POST':
		formulario = MascotasForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			datos['mensaje'] = "Datos guardados correctamente."

	return render(request, 'nuevaMascotaForm.html', datos)

def formMascotaMod(request, id):
	mascota = Mascotas.objects.get(id=id)
	datos = {
		'form' : MascotasForm(instance=mascota)
	}
	if request.method == 'POST':
		formulario = MascotasForm(data=request.POST, instance=mascota)
		if formulario.is_valid:
			formulario.save()
			datos['mensaje'] = "Datos modificados correctamente."
	return render(request, 'editarMascotaForm.html', datos)

def formMascotaDel(request, id):
	mascota = Mascotas.objects.get(id=id)
	mascota.delete()
	datos = {
		'form' : MascotasForm(instance=mascota)
	}
	if request.method == 'POST':
		formulario = MascotasForm(data=request.POST, instance=mascota)
		if formulario.is_valid:
			formulario.save()
			datos['mensaje'] = "Datos modificados correctamente."
	return redirect('listarMascotas')