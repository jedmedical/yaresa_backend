# Generated by Django 2.1.1 on 2018-12-22 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20181221_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liver_function_test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('alt', models.CharField(max_length=255, null=True)),
                ('ast', models.CharField(max_length=255, null=True)),
                ('alp', models.CharField(max_length=255, null=True)),
                ('albumin', models.CharField(max_length=255, null=True)),
                ('total_protein', models.CharField(max_length=255, null=True)),
                ('bilirubin', models.CharField(max_length=255, null=True)),
                ('ggt', models.CharField(max_length=255, null=True)),
                ('pt', models.CharField(max_length=255, null=True)),
                ('liver_test_date', models.DateField()),
                ('next_liver_test', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.AuthUserDemographic')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]