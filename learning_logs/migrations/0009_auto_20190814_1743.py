# Generated by Django 2.1.4 on 2019-08-14 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0008_auto_20190814_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='art_type',
            field=models.CharField(choices=[('popu', '流行'), ('classics', '经典')], max_length=20),
        ),
    ]
