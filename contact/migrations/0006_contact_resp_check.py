# Generated by Django 5.1 on 2024-12-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_contact_respondido_em'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='resp_check',
            field=models.BooleanField(default=False, verbose_name='Respondido?'),
        ),
    ]
