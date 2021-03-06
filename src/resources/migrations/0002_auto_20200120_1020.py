# Generated by Django 2.2.8 on 2020-01-20 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='description',
            new_name='abstract',
        ),
        migrations.AddField(
            model_name='resource',
            name='about',
            field=models.CharField(default='sts', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='aggregateRating',
            field=models.CharField(default='aa', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='audience',
            field=models.CharField(default='aa', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='image',
            field=models.CharField(default='img', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='inLanguage',
            field=models.CharField(default='en', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='keywords',
            field=models.CharField(default='key', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='license',
            field=models.CharField(default='license', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='publisher',
            field=models.CharField(default='publisher', max_length=100),
            preserve_default=False,
        ),
    ]
