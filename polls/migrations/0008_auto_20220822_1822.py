# Generated by Django 3.2.15 on 2022-08-22 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20220822_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invitemarried_request',
            old_name='lastName',
            new_name='fullName',
        ),
        migrations.RenameField(
            model_name='invitemarried_request',
            old_name='maleName',
            new_name='titleName',
        ),
    ]
