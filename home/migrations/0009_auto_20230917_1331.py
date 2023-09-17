# Generated by Django 3.2.20 on 2023-09-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_galerie_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galerie',
            name='categorie',
            field=models.CharField(blank=True, choices=[('REALISATIONS', 'REALISATIONS'), ('RENCONTRES', 'RENCONTRES'), ('PROJETS', 'PROJETS'), ('EVENEMENTS', 'EVENEMENTS')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='multimedia',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]