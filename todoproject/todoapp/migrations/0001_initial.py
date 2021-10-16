# Generated by Django 3.2.7 on 2021-10-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('isFinished', models.BooleanField(default=True)),
                ('date', models.DateTimeField(default='10:42 16/10/2021')),
            ],
        ),
    ]
