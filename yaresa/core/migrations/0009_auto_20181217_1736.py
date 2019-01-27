# Generated by Django 2.1.1 on 2018-12-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20181217_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='full_blood_count',
            name='lymphocyte',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='full_blood_count',
            name='neutrophil',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='full_blood_count',
            name='test_scan',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]