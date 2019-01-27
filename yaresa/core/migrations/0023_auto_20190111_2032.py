# Generated by Django 2.1.1 on 2019-01-11 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_prostate_specific_antigen_psa_scan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urine_test',
            name='ketone',
        ),
        migrations.RemoveField(
            model_name='urine_test',
            name='specific_gravity_test',
        ),
        migrations.AddField(
            model_name='fasting_blood_sugar',
            name='docs_comments',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='fasting_blood_sugar',
            name='next_fbs_test',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='full_blood_count',
            name='docs_comments',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='lipid_profile',
            name='docs_comments',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='liver_function_test',
            name='docs_comments',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='renal_function_test',
            name='docs_comments',
            field=models.CharField(max_length=3000, null=True),
        ),
    ]
