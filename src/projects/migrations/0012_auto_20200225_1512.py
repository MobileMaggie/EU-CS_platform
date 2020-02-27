# Generated by Django 2.2.10 on 2020-02-25 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0011_auto_20200225_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='nvoters',
        ),
        migrations.RemoveField(
            model_name='project',
            name='rate',
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.DecimalField(decimal_places=1, max_digits=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='uvote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Votes'),
        ),
    ]