# Generated by Django 4.2 on 2023-06-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_addblogmodel_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addblogmodel',
            name='img_content',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
