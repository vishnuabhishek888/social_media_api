# Generated by Django 4.1.7 on 2023-05-04 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follow',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], default='None', max_length=20, null=True),
        ),
    ]
