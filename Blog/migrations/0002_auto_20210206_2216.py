# Generated by Django 3.1.5 on 2021-02-06 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catergoria',
            new_name='Categoria',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
    ]