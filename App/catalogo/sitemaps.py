# tienda/sitemaps.py
from django.contrib.sitemaps import Sitemap
from .models import Producto 

class ProductoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8 

    def items(self):
        return Producto.objects.all()
