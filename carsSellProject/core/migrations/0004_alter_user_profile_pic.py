# Generated by Django 4.0.4 on 2022-05-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='media/profile_pics/default.jpg', upload_to='profile_pics/'),
        ),
    ]
