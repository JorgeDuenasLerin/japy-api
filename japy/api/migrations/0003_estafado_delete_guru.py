# Generated by Django 5.0.2 on 2024-02-25 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_criptomoneda_guru'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estafado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('cripto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estafados', to='api.criptomoneda')),
            ],
        ),
        migrations.DeleteModel(
            name='Guru',
        ),
    ]
