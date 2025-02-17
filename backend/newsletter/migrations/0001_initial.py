# Generated by Django 5.1.4 on 2025-02-14 10:29

import newsletter.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255)),
                ('cover', models.ImageField(upload_to=newsletter.models.news_letter_image_cover)),
                ('caption', models.TextField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='NewsLetterSubscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('subscribed_at', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('newsletters_to_send', models.ManyToManyField(related_name='newsletters', to='newsletter.newsletter')),
            ],
            options={
                'verbose_name': 'NewsLetter Subscriber',
                'verbose_name_plural': 'NewsLetter Subscribers',
                'ordering': ['-id'],
            },
        ),
    ]
