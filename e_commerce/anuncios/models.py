from django.db import models
from django.utils.text import slugify

class Categoria(models.Model):
    titulo = models.CharField(max_length=40)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['titulo']

class Anuncio(models.Model):
    titulo = models.CharField(max_length=40)
    slug = models.SlugField(unique=True)
    descricao = models.TextField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-id']

class Midia(models.Model):
    TIPO_CHOICES = (
        ('imagem', 'Imagem'),
        ('video', 'Vídeo'),
    )
    anuncio = models.ForeignKey(Anuncio, related_name='midias', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    url = models.URLField()

    def __str__(self):
        return f"{self.tipo} - {self.url}"
