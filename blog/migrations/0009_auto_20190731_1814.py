# Generated by Django 2.2.3 on 2019-07-31 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190731_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='menu',
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Menu'),
        ),
    ]
