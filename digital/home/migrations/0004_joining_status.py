# Generated by Django 2.0.1 on 2019-10-18 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20191012_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='joining',
            name='status',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]
