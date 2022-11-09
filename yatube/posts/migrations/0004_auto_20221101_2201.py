# Generated by Django 2.2.16 on 2022-11-01 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20221028_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(
                help_text='Введите описание группы',
                verbose_name='Описание группы',
            ),
        ),
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(
                help_text='Введите метку группы',
                unique=True,
                verbose_name='Метка группы',
            ),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(
                help_text='Введите название группы',
                max_length=200,
                verbose_name='Название группы',
            ),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(
                auto_now_add=True,
                help_text='Введите дату публикации поста',
                verbose_name='Дата публикации',
            ),
        ),
    ]