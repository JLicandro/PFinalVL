# Generated by Django 4.0.4 on 2022-06-26 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_blogmodel_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogmodel',
            old_name='fecha_creacion',
            new_name='creacion',
        ),
        migrations.RenameField(
            model_name='blogmodel',
            old_name='subtitulo',
            new_name='subtitulo',
        ),
    ]