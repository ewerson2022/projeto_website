# Generated by Django 4.2.1 on 2023-06-04 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_cadastro_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro_usuario',
            name='email',
            field=models.EmailField(max_length=30, unique=True),
        ),
    ]