# Generated by Django 2.1.1 on 2018-12-26 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_liver_function_test_bilirubin_direct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prostate_specific_antigen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('psa_total', models.CharField(max_length=255, null=True)),
                ('psa_test_date', models.DateField()),
                ('next_psa_text', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.AuthUserDemographic')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
