from django.db import models
from django.utils.text import slugify

class Categoria(models.Model):
    titulo = models.CharField(max_length=40)
    slug = models.SlugField(unique=True)  # Add the slug field

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)  # Generate the slug do titulo
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['titulo']

class Anuncio(models.Model):
    titulo = models.CharField(max_length=40)
    slug = models.SlugField(unique=True)  # Add the slug field
    imagem = models.ImageField(upload_to='static/img/')
    descricao = models.TextField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-id']
