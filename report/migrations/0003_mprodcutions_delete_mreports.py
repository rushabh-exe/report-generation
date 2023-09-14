# Generated by Django 4.2.5 on 2023-09-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_remove_mreports_fyyear_remove_mreports_amt_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mprodcutions',
            fields=[
                ('srno', models.AutoField(primary_key=True, serialize=False)),
                ('Subs', models.CharField(max_length=255)),
                ('target', models.FloatField(default=0)),
                ('fyno', models.FloatField(default=0)),
                ('Achmt', models.FloatField(default=0)),
                ('pastfyno', models.FloatField(default=0)),
                ('growth', models.FloatField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Mreports',
        ),
    ]
