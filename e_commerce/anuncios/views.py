# views.py
from django.shortcuts import render, get_object_or_404
from .models import Categoria, Anuncio

def postagens(request):
    categorias = Categoria.objects.all()
    ultimos_anuncios = Anuncio.objects.all()[:12]
    return render(request, 'postagens.html', {'categorias': categorias, 'anuncios': ultimos_anuncios})

def categoria(request, categoria_id): # Adicione o parâmetro categoria_id
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categorias = Categoria.objects.all()
    anuncios = Anuncio.objects.filter(categoria=categoria)
    return render(request, 'categoria.html', {'categorias': categorias, 'anuncios': anuncios, 'categoria': categoria})

def anuncio(request, anuncio_id):  # Adicione o parâmetro anuncio_id
    anuncio_obj = get_object_or_404(Anuncio, id=anuncio_id)  # Use anuncio_id para recuperar o anúncio
    categorias = Categoria.objects.all()
    return render(request, 'anuncio.html', {'categorias': categorias, 'anuncio': anuncio_obj})
