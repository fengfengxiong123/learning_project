# Generated by Django 2.1.4 on 2019-05-31 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0006_auto_20190528_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artcontent',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_logs.Article', verbose_name='文章'),
        ),
    ]
