# Generated by Django 4.0.6 on 2022-07-06 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_book_book_hoto_alter_user_is_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_hoto',
            new_name='book_photo',
        ),
    ]
