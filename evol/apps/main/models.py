from django.db import models

class News(models.Model):
	"""
	Representa una noticia.
	"""

	title = models.CharField(max_length=40)
	body  = models.TextField(max_length=300)

	class Meta:
		verbose_name_plural = "Noticias"

	def __unicode__(self):
		return self.title