# Generated by Django 2.1.1 on 2018-09-26 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUserDemographic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('unique_id', models.CharField(max_length=255, null=True)),
                ('surname', models.CharField(max_length=255, null=True, verbose_name='Surname')),
                ('sex', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE')], default='Male', max_length=255, verbose_name='Gender')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('nationality', models.CharField(max_length=255, null=True)),
                ('religion', models.CharField(max_length=255, null=True)),
                ('marital_status', models.CharField(choices=[('Married', 'MARRIED'), ('Single', 'SINGLE')], default='Single', max_length=255)),
                ('address', models.CharField(max_length=255, null=True)),
                ('occupation', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mobile', models.CharField(max_length=255, null=True)),
                ('emergency_contact_name', models.CharField(max_length=255, null=True)),
                ('emergency_contact_mobile', models.CharField(max_length=255, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Blood_Pressure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bp', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.AuthUserDemographic')),
            ],
        ),
        migrations.CreateModel(
            name='Height',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.AuthUserDemographic')),
            ],
        ),
        migrations.CreateModel(
            name='Med_graphic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=255, null=True)),
                ('sickling_status', models.CharField(choices=[('AA', 'AA'), ('AS', 'AS'), ('SS', 'SS'), ('SC', 'SC')], max_length=255, null=True)),
                ('g6pd_status', models.CharField(choices=[('Normal', 'Normal'), ('Partial Defect', 'Partial Defect'), ('Full Defect', 'Full Defect')], max_length=255, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.AuthUserDemographic')),
            ],
        ),
        migrations.CreateModel(
            name='Medical_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('diabetes_mellitus', models.BooleanField(default=False)),
                ('systematic_hypertension', models.BooleanField(default=False)),
                ('epilepsy', models.BooleanField(default=False)),
                ('others', models.CharField(max_length=300, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.AuthUserDemographic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Social_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('alcohol', models.BooleanField(default=False)),
                ('smoking', models.BooleanField(default=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.AuthUserDemographic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.AuthUserDemographic')),
            ],
        ),
    ]