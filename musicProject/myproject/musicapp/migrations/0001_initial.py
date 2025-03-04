# Generated by Django 5.0.3 on 2024-06-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistClassify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_classify', models.CharField(max_length=255)),
                ('artist_name', models.CharField(max_length=255)),
                ('category_id', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'artist_classify',
            },
        ),
    ]
