# Generated by Django 3.0.6 on 2020-06-10 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birdsong', '0002_auto_20200603_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
