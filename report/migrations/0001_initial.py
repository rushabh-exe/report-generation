# Generated by Django 4.2.5 on 2023-09-14 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mreports',
            fields=[
                ('srno', models.AutoField(primary_key=True, serialize=False)),
                ('Subs', models.CharField(max_length=200)),
                ('target', models.IntegerField(default=0)),
                ('FYyear', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('amt', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('profit', models.IntegerField(default=0)),
            ],
        ),
    ]
