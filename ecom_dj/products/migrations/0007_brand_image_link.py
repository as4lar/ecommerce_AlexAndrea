# Generated by Django 4.2 on 2023-05-15 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_image_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image_link',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
