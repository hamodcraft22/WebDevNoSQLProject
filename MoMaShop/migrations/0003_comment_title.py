# Generated by Django 4.1 on 2022-12-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MoMaShop", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="title",
            field=models.CharField(default="hello", max_length=150),
            preserve_default=False,
        ),
    ]
