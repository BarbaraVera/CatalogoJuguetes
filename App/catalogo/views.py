from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto
from django.db.models import Q 
from django.core.paginator import Paginator

def home(request):
    productos_destacados = Producto.objects.filter(destacado=True, stock__gt=0)
    
    categorias = Categoria.objects.all()

    context = {
        'productos_destacados': productos_destacados,
        'categorias': categorias,
    }
    return render(request, 'catalogo/home.html', context)

def lista_productos(request):
    query = request.GET.get('q')
    ordenar_seleccionado = request.GET.get('ordenar', 'populares')
    categoria_seleccionada = request.GET.get('categoria')
    precio_max_seleccionado = request.GET.get('precio_max')

    productos = Producto.objects.filter(stock__gt=0)

    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        ).distinct()

    if categoria_seleccionada:
        productos = productos.filter(categoria__id=categoria_seleccionada)

    if precio_max_seleccionado:
        productos = productos.filter(precio__lte=precio_max_seleccionado) 

    if ordenar_seleccionado == 'precio_asc':
        productos = productos.order_by('precio')
    elif ordenar_seleccionado == 'precio_desc':
        productos = productos.order_by('-precio')
    else: 
        productos = productos.order_by('-id')
    
    paginator = Paginator(productos, 12) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categorias = Categoria.objects.all()
    
    context = {
        'productos': page_obj,
        'categorias': categorias,
        'ordenar_seleccionado': ordenar_seleccionado,
        'categoria_seleccionada': categoria_seleccionada,
        'precio_max_seleccionado': precio_max_seleccionado,
        'query': query, 
    }
    return render(request, 'catalogo/lista_productos.html', context)

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    productos_relacionados = Producto.objects.filter(
        categoria=producto.categoria
    ).exclude(pk=pk)[:4] 

    context = {
        'producto': producto,
        'productos_relacionados': productos_relacionados
    }
    return render(request, 'catalogo/detalle_producto.html', context)