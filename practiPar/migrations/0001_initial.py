# Generated by Django 4.2.5 on 2023-09-29 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ordenes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCliente', models.CharField(max_length=150)),
                ('total', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
