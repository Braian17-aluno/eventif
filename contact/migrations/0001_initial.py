# Generated by Django 5.1 on 2024-11-25 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100, verbose_name="nome")),
                ("telefone", models.CharField(max_length=20, verbose_name="telefone")),
                ("email", models.EmailField(max_length=254, verbose_name="e-mail")),
                (
                    "menssagem",
                    models.CharField(max_length=200, verbose_name="menssagem"),
                ),
            ],
        ),
    ]
