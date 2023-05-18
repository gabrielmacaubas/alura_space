from django.contrib import admin
from apps.galeria.models import Fotografia, Categoria


class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('categoria', 'usuario')
    list_editable = ('publicada',)
    list_per_page = 10


class ListandoCategorias(admin.ModelAdmin):
    list_display = ('id', 'categoria')
    list_display_links = ('id', 'categoria')
    search_fields = ('categoria',)

admin.site.register(Fotografia, ListandoFotografias)
admin.site.register(Categoria, ListandoCategorias)
