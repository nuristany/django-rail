# Generated by Django 5.0.3 on 2024-03-29 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_itemimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['user__first_name', 'user__last_name']},
        ),
    ]
