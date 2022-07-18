from django.db import models

# Create your models here.

class Kelompok(models.Model):
    nama = models.CharField(max_length=100)
    keterangan = models.TextField()
    def __str__(self):
        return self.nama

class Buku(models.Model):
    judul = models.CharField(max_length=100)
    penulis = models.CharField(max_length=100)
    penerbit = models.CharField(max_length=100)
    jumlah_buku = models.IntegerField(null=True)
    kelompok_id = models.ForeignKey(Kelompok, on_delete=models.CASCADE, null=True)
    cover = models.ImageField(upload_to='cover/', null=True)
    tanggal = models.DateField(auto_now_add=True, null=True)
    waktu = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.judul

class Penerbit(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    telepon = models.CharField(max_length=100)
    def __str__(self):
        return self.nama