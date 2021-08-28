# Generated by Django 3.2.5 on 2021-08-12 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0003_rename_notas_author_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='Authors', to='books_authors_app.Book'),
        ),
    ]
