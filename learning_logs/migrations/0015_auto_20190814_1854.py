# Generated by Django 2.1.4 on 2019-08-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0014_auto_20190814_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='art_type',
            field=models.CharField(choices=[('lx', (('1', '玄幻'), ('2', '奇幻'), ('3', '科幻'), ('4', '武侠'), ('5', '仙侠'), ('5', '都市'), ('6', '言情'), ('7', '历史'))), ('jd', (('1', '名著'), ('2', '神话'), ('3', '小说'), ('4', '诸子'), ('5', '诗词'), ('6', '史书')))], max_length=20),
        ),
    ]
