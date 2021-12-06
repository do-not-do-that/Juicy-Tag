# Generated by Django 3.0.7 on 2021-12-06 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Juicy_list',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('pcode', models.CharField(max_length=4)),
                ('user_id', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField(max_length=2000)),
                ('is_complete', models.BooleanField()),
                ('created_at', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'juicy_list',
                'managed': False,
            },
        ),
    ]
