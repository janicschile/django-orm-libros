# Generated by Django 3.2.5 on 2021-08-12 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_author_notas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='notas',
            new_name='note',
        ),
    ]
