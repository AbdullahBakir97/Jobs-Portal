# Generated by Django 4.2.7 on 2023-11-08 02:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('image', models.ImageField(upload_to='categories', verbose_name='Image')),
                ('job_count', models.IntegerField(max_length=100000, verbose_name='Job Count')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('logo', models.ImageField(upload_to='company', verbose_name='Logo')),
                ('presentation', models.TextField(max_length=10000, verbose_name='Presentation')),
                ('website', models.TextField(max_length=300, verbose_name='Website')),
                ('email', models.TextField(max_length=300, verbose_name='Email')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('location', models.CharField(max_length=150, verbose_name='Location')),
                ('salary', models.FloatField(verbose_name='Salary')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at')),
                ('vacancy', models.IntegerField(verbose_name='Vacancy')),
                ('job_nature', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Remote', 'Remote'), ('Freelance', 'Freelance')], max_length=20, verbose_name='Job Nature')),
                ('application_date', models.DateField(verbose_name='Application Date')),
                ('description', models.TextField(max_length=50000, verbose_name='Description')),
                ('knowledge_requirements', models.TextField(max_length=10000, verbose_name='Knowledge Requirements')),
                ('education_experience', models.TextField(max_length=10000, verbose_name='Education Experience')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('agency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_company', to='jobs.company', verbose_name='Company')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_category', to='jobs.category', verbose_name='Category')),
            ],
        ),
    ]
