# Generated by Django 4.2 on 2024-11-20 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='estatus',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('en progreso', 'En progreso'), ('completado', 'Completado')], default='pendiente', max_length=15),
        ),
    ]
