# Generated by Django 2.2.5 on 2020-03-05 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20200303_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='activedirectoryasset',
            name='ad_account_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]