# Generated by Django 5.0.7 on 2024-07-26 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_githaburl_user_instagramurl_user_linkedinurl_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photoPresentationUrl',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
