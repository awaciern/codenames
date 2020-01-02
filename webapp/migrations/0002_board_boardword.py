# Generated by Django 3.0.1 on 2019-12-31 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('color', models.CharField(choices=[('R', 'Red'), ('B', 'Blue'), ('N', 'Neutral'), ('X', 'Assasin')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.ManyToManyField(to='webapp.BoardWord')),
            ],
        ),
    ]
