# Generated by Django 2.2.5 on 2020-03-03 15:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20200303_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privilege',
            name='id',
            field=models.UUIDField(default=uuid.UUID('403a3149-997a-4094-8c75-dede381c3659'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='staff',
            name='id',
            field=models.UUIDField(default=uuid.UUID('636ab8cb-bee5-4c7e-86cd-26923c736c9e'), editable=False, primary_key=True, serialize=False),
        ),
    ]