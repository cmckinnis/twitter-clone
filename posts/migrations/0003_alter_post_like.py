# Generated by Django 4.1.4 on 2022-12-15 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_body_alter_post_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='like'),
        ),
    ]