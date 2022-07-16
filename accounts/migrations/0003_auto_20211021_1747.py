# Generated by Django 3.2.8 on 2021-10-21 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211020_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, null=True)),
                ('description', models.TextField(null=True)),
                ('updates', models.TextField(blank=True, default='')),
                ('status', models.CharField(default='active', max_length=10)),
                ('short_description', models.CharField(blank=True, max_length=50, null=True)),
                ('request_image', models.ImageField(null=True, upload_to='customers')),
                ('under_investigation_by', models.CharField(blank=True, max_length=1000, null=True)),
                ('complaint_filer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]