# Generated by Django 4.0.4 on 2022-05-10 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_user_profile_pic_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='car_pic',
            field=models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/'),
        ),
    ]
