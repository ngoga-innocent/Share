# Generated by Django 5.1.5 on 2025-05-24 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_ourimpact_story_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourimpact',
            name='story',
            field=models.TextField(),
        ),
    ]
