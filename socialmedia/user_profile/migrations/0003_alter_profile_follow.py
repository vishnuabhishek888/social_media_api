# Generated by Django 4.1.7 on 2023-05-04 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_profile_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follow',
            field=models.CharField(choices=[('follow', 'Follow'), ('unfollow', 'Unfollow')], default='None', max_length=20, null=True),
        ),
    ]
