# Generated by Django 2.0.4 on 2018-05-07 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ojss_app', '0003_auto_20180507_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_role', models.CharField(max_length=255)),
                ('job_description', models.CharField(max_length=255)),
                ('organization', models.CharField(max_length=255)),
                ('remuneration', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('skill_required_1', models.CharField(max_length=255)),
                ('skill_required_2', models.CharField(max_length=255)),
                ('skill_required_3', models.CharField(blank=True, max_length=255, null=True)),
                ('skill_required_4', models.CharField(blank=True, max_length=255, null=True)),
                ('skill_required_5', models.CharField(blank=True, max_length=255, null=True)),
                ('deadline', models.DateField()),
                ('posted_date', models.DateField(auto_now_add=True)),
                ('job_ad_flag', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='RecruiterProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='M', max_length=1)),
                ('company_name', models.CharField(max_length=255)),
                ('company_description', models.CharField(max_length=255)),
                ('company_address', models.CharField(max_length=255)),
                ('company_phone', models.IntegerField()),
                ('job_role', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='recruiter_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ojss_app.RecruiterProfile'),
        ),
    ]
