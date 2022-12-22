# Generated by Django 4.1 on 2022-12-22 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MoMaShop", "0002_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.CharField(
                choices=[
                    ("si", "Still Image"),
                    ("ai", "Animated Image"),
                    ("cv", "Customized Video"),
                ],
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="paymentType",
            field=models.CharField(
                choices=[("cc", "Credit Card"), ("dc", "Debit Card")], max_length=2
            ),
        ),
    ]
