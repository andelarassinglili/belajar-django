from django.contrib import admin
from glcm.models import Buku, Kelompok
# Register your models here.

class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul', 'penulis', 'kelompok_id', 'jumlah_buku']
    search_fields = ['judul', 'penulis', 'penerbit']
    list_filter = ['kelompok_id']
    list_per_page = 4
    ordering = ['judul']

admin.site.register(Buku, BukuAdmin)
admin.site.register(Kelompok)
