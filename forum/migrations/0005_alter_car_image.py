# Generated by Django 5.1.6 on 2025-03-27 20:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("forum", "0004_alter_customuser_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/car_images/"
            ),
        ),
    ]
