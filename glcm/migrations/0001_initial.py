# Generated by Django 4.0.6 on 2022-07-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('penulis', models.CharField(max_length=100)),
                ('penerbit', models.CharField(max_length=100)),
            ],
        ),
    ]