# Generated by Django 4.2 on 2023-06-10 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0005_alter_addblogmodel_img_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addblogmodel',
            old_name='img_content',
            new_name='blog_img',
        ),
    ]
