# Generated by Django 2.2.6 on 2020-02-13 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitars', '0006_remove_guitars_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitars',
            name='color',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]