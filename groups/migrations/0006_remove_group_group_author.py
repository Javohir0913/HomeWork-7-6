# Generated by Django 4.2.16 on 2024-10-07 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_alter_groupview_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='group_author',
        ),
    ]
