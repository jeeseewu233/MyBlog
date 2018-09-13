# Generated by Django 2.1 on 2018-08-29 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_imgurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='category',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
    ]