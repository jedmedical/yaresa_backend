# Generated by Django 2.1.1 on 2018-10-04 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuserdemographic',
            name='other_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='authuserdemographic',
            name='picture',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
        migrations.AddField(
            model_name='authuserdemographic',
            name='title',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
