# Generated by Django 3.2.4 on 2021-06-21 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0005_album_personnel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='personnel',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]