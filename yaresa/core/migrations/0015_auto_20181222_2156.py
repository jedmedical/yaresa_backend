# Generated by Django 2.1.1 on 2018-12-22 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_liver_function_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liver_function_test',
            name='pt',
        ),
        migrations.AddField(
            model_name='liver_function_test',
            name='liver_scan',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]
