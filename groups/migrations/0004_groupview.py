# Generated by Django 4.2.16 on 2024-10-07 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0003_honadon'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups_list', models.ManyToManyField(to='groups.group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Group View',
                'verbose_name_plural': 'Group Views',
                'db_table': 'groupview',
            },
        ),
    ]
