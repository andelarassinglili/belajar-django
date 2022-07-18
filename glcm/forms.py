from tkinter import Widget
from django.forms import ModelForm
from glcm.models import Buku
from django import forms

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'
        # exclude = ['jumlah_buku']
        # fields = ['judul', 'penulis', 'kelompok_id']

        widgets = {
            'judul' : forms.TextInput({'class':'form-control', 'id':'inputjudul'}),
            'penulis' : forms.TextInput({'class':'form-control'}),
            'penerbit' : forms.TextInput({'class':'form-control'}),
            'jumlah_buku' : forms.NumberInput({'class':'form-control'}),
            'kelompok_id' : forms.Select({'class':'form-control'}),
        }


