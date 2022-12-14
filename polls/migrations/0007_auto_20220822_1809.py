# Generated by Django 3.2.15 on 2022-08-22 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_invitemarried_request_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invitemarried_request',
            old_name='image',
            new_name='invite_picture',
        ),
        migrations.RenameField(
            model_name='invitemarried_request',
            old_name='clock',
            new_name='lastName',
        ),
        migrations.RemoveField(
            model_name='invitemarried_request',
            name='femaleName',
        ),
        migrations.RemoveField(
            model_name='invitemarried_request',
            name='location',
        ),
        migrations.AddField(
            model_name='invitemarried_request',
            name='male_picture',
            field=models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to=''),
        ),
    ]
