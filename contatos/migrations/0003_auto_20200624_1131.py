# Generated by Django 3.0.7 on 2020-06-24 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_contato_mostra'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='mostra',
            new_name='mostrar',
        ),
    ]