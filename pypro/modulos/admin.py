from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from pypro.modulos.models import Modulo, Aula


@admin.register(Modulo)
class ModelAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'publico', 'move_up_down_links')
    prepopulated_fields = {'slug': ('titulo',)}


@admin.register(Aula)
class AulaAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'modulo', 'move_up_down_links')
    list_filter = ('modulo',)
    prepopulated_fields = {'slug': ('titulo',)}