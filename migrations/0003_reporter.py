# Generated by Django 2.0.9 on 2019-02-14 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lid', '0002_match_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('outlet', models.CharField(blank=True, max_length=50, null=True)),
                ('statecode', models.CharField(max_length=2)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
