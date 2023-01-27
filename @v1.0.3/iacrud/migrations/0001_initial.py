# Generated by Django 4.1.5 on 2023-01-27 00:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IaCrud',
            fields=[
                ('id_base_de_dados', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('historia', models.CharField(max_length=250)),
                ('divida', models.CharField(max_length=250)),
                ('garantia', models.CharField(max_length=250)),
                ('renda', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]