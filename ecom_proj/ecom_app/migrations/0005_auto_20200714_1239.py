# Generated by Django 2.2.4 on 2020-07-14 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0004_auto_20200714_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='expiration_date',
            field=models.DateField(max_length=8),
        ),
    ]
