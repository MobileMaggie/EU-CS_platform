# Generated by Django 2.2.8 on 2020-01-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('datePublished', models.DateTimeField(verbose_name='Date Published')),
            ],
        ),
    ]