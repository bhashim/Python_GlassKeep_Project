# Generated by Django 2.2.4 on 2020-07-14 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0002_auto_20200714_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='expiration_date',
            field=models.FloatField(),
        ),
    ]