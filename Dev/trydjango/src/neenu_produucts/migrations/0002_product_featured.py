# Generated by Django 2.1.7 on 2025-01-16 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neenu_produucts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
