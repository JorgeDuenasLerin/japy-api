# Generated by Django 5.0.2 on 2024-03-12 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_cuadro'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuadro',
            name='color',
            field=models.CharField(default='#FF00FF', max_length=200),
            preserve_default=False,
        ),
    ]