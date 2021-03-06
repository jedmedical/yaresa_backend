# Generated by Django 2.1.1 on 2018-12-18 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20181217_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lipid_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_cholesterol', models.CharField(max_length=255, null=True)),
                ('hdl_cholesterol', models.CharField(max_length=255, null=True)),
                ('ldl_cholesterol', models.CharField(max_length=255, null=True)),
                ('triglycerides', models.CharField(max_length=255, null=True)),
                ('date', models.DateField()),
                ('next_lipid_test', models.DateField()),
                ('lipid_scan', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.AuthUserDemographic')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
