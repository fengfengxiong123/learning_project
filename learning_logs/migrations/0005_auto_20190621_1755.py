# Generated by Django 2.1.4 on 2019-06-21 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_auto_20190621_1753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artchapter',
            options={'ordering': ['chapter_name']},
        ),
    ]
