# Generated by Django 3.2.25 on 2024-05-13 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectNE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(default=None, max_length=100)),
                ('username', models.CharField(default='temp', max_length=100)),
                ('password', models.CharField(default='root', max_length=100)),
                ('hostname', models.CharField(default=None, max_length=100)),
                ('port_number', models.IntegerField(default=22)),
                ('interface', models.CharField(default='CLI', max_length=50)),
            ],
        ),
    ]