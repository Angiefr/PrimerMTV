# Generated by Django 4.0.5 on 2022-06-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('edad', models.PositiveBigIntegerField()),
                ('nacimiento', models.DateTimeField()),
            ],
        ),
    ]
