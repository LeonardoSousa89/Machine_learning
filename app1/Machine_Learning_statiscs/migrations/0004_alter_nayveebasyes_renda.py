# Generated by Django 4.1.5 on 2023-01-24 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Machine_Learning_statiscs', '0003_alter_nayveebasyes_renda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nayveebasyes',
            name='renda',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]
