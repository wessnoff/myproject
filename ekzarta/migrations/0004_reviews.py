# Generated by Django 2.0.2 on 2019-01-10 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekzarta', '0003_auto_20180706_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_name', models.TextField(max_length=100)),
                ('v_review', models.TextField(max_length=300)),
            ],
        ),
    ]
