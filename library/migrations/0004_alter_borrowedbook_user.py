# Generated by Django 5.1.7 on 2025-03-20 20:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_borrowedbook_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowedbook',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books', to=settings.AUTH_USER_MODEL),
        ),
    ]
