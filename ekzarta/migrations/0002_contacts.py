# Generated by Django 2.0.2 on 2018-07-06 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekzarta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_1', models.TextField(max_length=13, null=True)),
                ('phone_2', models.TextField(max_length=13, null=True)),
                ('phone_3', models.TextField(max_length=13, null=True)),
                ('address', models.TextField(max_length=100, null=True)),
                ('city', models.TextField(max_length=100, null=True)),
            ],
        ),
    ]
