# Generated by Django 3.1.2 on 2020-10-29 11:46

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
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='')),
                ('specialization', models.CharField(max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teaches', to='cms.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(blank=True, null=True, upload_to='')),
                ('DOB', models.DateField()),
                ('tenth_marks', models.FloatField(default=0)),
                ('inter_marks', models.FloatField(default=0)),
                ('current_marks', models.FloatField(default=0)),
                ('branch', models.CharField(choices=[('Computer Science & Engineering', 'Computer Science & Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Others', 'Others')], default='Computer Science & Engineering', max_length=100)),
                ('year', models.IntegerField(choices=[(1, 'Ist Year'), (2, 'IInd Year'), (3, 'IIIrd Year'), (4, 'IVth Year')], default=1)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SelectedSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='selected', to='cms.student')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studies', to='cms.subject')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('type', models.IntegerField(choices=[(1, 'Sick'), (2, 'Casual'), (3, 'Earned')], default=3)),
                ('status', models.IntegerField(choices=[(1, 'Accepted'), (2, 'Rejected'), (3, 'Pending')], default=3)),
                ('reason', models.CharField(max_length=900)),
                ('verdict', models.CharField(max_length=900, null=True)),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request', to='cms.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casual_leave', models.IntegerField(default=7)),
                ('earned_leave', models.IntegerField(default=10)),
                ('sick_leave', models.IntegerField(default=8)),
                ('faculty', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(null=True)),
                ('present', models.BooleanField()),
                ('selected_subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to='cms.selectedsubject')),
            ],
        ),
    ]
