# Generated by Django 4.2 on 2023-06-10 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0004_alter_addblogmodel_img_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addblogmodel',
            name='img_content',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
