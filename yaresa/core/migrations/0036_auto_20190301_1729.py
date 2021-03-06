# Generated by Django 2.1.1 on 2019-03-01 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_medication_strength'),
    ]

    operations = [
        migrations.AddField(
            model_name='surgery',
            name='docs_comments',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='authuserdemographic',
            name='marital_status',
            field=models.CharField(choices=[('Married', 'MARRIED'), ('Single', 'SINGLE'), ('Widowed', 'WIDOWED'), ('Divorced', 'DIVORCED')], default='Single', max_length=255),
        ),
    ]
