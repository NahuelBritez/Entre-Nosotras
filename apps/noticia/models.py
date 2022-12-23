from django.db import models
from apps.users.models import Usuario

class Categoria(models.Model):
	nombre = models.CharField(max_length = 60)

	def __str__(self):
		return self.nombre

class Noticia(models.Model):

	titulo = models.CharField(max_length = 150)
	subtitulo = models.CharField(max_length=100, null=True, blank=True)
	cuerpo = models.TextField()
	imagen = models.ImageField(upload_to = 'noticias')
	categoria_noticia = models.ForeignKey(Categoria, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Titulo: {self.titulo} // Categoria: {self.categoria_noticia}"

class Comentario(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	texto = models.TextField(max_length = 1500)
	noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-fecha']

	def __str__(self):
		return '%s - %s' % (self.noticia.titulo, self.nombre)
		# return f"Usuario: {self.usuario}  //  Comentario: {self.texto}"

