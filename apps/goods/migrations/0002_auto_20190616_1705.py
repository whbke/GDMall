# Generated by Django 2.0.6 on 2019-06-16 17:05

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsimage',
            name='content',
            field=mdeditor.fields.MDTextField(verbose_name='内容'),
        ),
    ]
