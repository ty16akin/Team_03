# Generated by Django 4.2.6 on 2023-11-21 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CHBS', '0003_rename_digital_product_special'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False, null=True),
        ),
    ]