# Generated by Django 4.1.1 on 2022-09-10 07:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('category_name', models.CharField(max_length=50)),
                ('category_icon', models.ImageField(blank=True, null=True, upload_to='category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='generalcasemodel',
            name='latittude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='generalcasemodel',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='generalcasemodel',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='related_category_cases', to='app.categorymodel'),
            preserve_default=False,
        ),
    ]