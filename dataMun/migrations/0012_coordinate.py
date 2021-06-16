# Generated by Django 3.2.4 on 2021-06-16 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataMun', '0011_paciente_cant_casos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lattitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
            ],
        ),
    ]
