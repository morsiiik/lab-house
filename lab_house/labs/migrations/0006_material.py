# Generated by Django 3.2.9 on 2021-12-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0005_mentorcounter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('url', models.URLField(verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материалы',
                'ordering': ['pk'],
            },
        ),
    ]
