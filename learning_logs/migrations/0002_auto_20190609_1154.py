# Generated by Django 2.1.4 on 2019-06-09 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artcontent',
            options={'ordering': ['chapter_add_date']},
        ),
    ]
