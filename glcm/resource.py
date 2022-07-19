from dataclasses import fields
from import_export import resources
from glcm.models import Buku
from import_export.fields import Field
from import_export import resources

class BukuResource(resources.ModelResource):
    kelompok_id__nama = Field(attribute='kelompok_id', column_name='Kelompok')
    class Meta:
        model = Buku
        fields = ['judul', 'tanggal', 'penerbit', 'jumlah_buku', 'kelompok_id__nama', 'penulis', 'waktu']
        export_order = ['judul', 'tanggal', 'waktu', 'penerbit', 'jumlah_buku', 'kelompok_id__nama', 'penulis']