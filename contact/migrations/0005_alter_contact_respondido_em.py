# Generated by Django 5.1 on 2024-12-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_contact_respondido_em'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='respondido_em',
            field=models.DateTimeField(blank=True, null=True, verbose_name='respondido em'),
        ),
    ]
