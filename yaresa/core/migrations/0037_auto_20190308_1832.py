# Generated by Django 2.1.1 on 2019-03-08 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20190301_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='telephone',
            new_name='reps_email',
        ),
        migrations.AddField(
            model_name='organization',
            name='reps_contact',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
