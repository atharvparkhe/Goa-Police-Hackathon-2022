# Generated by Django 4.1.1 on 2022-09-11 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliceHeadModel',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rank', models.CharField(max_length=10)),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to='police_admin_profile')),
            ],
            options={
                'abstract': False,
            },
            bases=('base.baseuser',),
        ),
        migrations.CreateModel(
            name='PoliceModel',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rank', models.CharField(max_length=10)),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to='police_profile')),
            ],
            options={
                'abstract': False,
            },
            bases=('base.baseuser',),
        ),
    ]
