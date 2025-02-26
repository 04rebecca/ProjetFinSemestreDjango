# Generated by Django 5.1.6 on 2025-02-25 12:11

import django.db.models.deletion
import django.db.models.query
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionBoutique', '0002_alter_vente_produit'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/'),
        ),
        migrations.AlterField(
            model_name='vente',
            name='produit',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, on_delete=django.db.models.deletion.CASCADE, to='GestionBoutique.produit'),
        ),
    ]
