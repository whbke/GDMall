# Generated by Django 2.0.6 on 2019-06-16 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='wx_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.WxUser', verbose_name='微信用户'),
        ),
    ]
