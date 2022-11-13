from django.contrib import admin
from .models import Bares, Heladerias, Restaurantes, Avatar

class BarrappAdmin(admin.ModelAdmin):
    list_display = ("nombre","email","telefono")
    search_fields = ("nombre","telefono")

# Register your models here.
admin.site.register(Bares, BarrappAdmin)
admin.site.register(Heladerias, BarrappAdmin)
admin.site.register(Restaurantes, BarrappAdmin)
admin.site.register(Avatar)