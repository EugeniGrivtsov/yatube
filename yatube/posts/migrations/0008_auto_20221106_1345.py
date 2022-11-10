# Generated by Django 2.2.16 on 2022-11-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20221104_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(
                auto_now_add=True,
                db_index=True,
                help_text='Введите дату публикации поста',
                verbose_name='Дата публикации',
            ),
        ),
    ]
