# Generated by Django 4.0.3 on 2022-03-28 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proj',
            fields=[
                ('id', models.CharField(help_text='Adicione um ID com 16 caracteres', max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('company', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount_products', models.IntegerField()),
            ],
        ),
    ]
