# Generated by Django 2.0.1 on 2019-09-30 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Email', models.CharField(max_length=25)),
                ('Phone_no', models.CharField(max_length=10)),
                ('Course', models.CharField(max_length=25)),
                ('Source', models.CharField(max_length=25)),
            ],
        ),
    ]
