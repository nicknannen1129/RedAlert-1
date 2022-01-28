# Generated by Django 3.2.8 on 2021-12-08 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redAlertSite', '0002_auto_20211208_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='client_data',
        ),
    ]