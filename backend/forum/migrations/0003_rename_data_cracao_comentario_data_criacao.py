# Generated by Django 3.2.3 on 2021-06-03 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_rename_data_cracao_post_data_criacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='data_cracao',
            new_name='data_criacao',
        ),
    ]
