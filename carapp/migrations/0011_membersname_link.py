# Generated by Django 4.2.1 on 2023-06-11 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0010_membersname'),
    ]

    operations = [
        migrations.AddField(
            model_name='membersname',
            name='link',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
