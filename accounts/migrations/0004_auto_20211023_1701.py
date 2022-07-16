# Generated by Django 3.2.8 on 2021-10-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211021_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='short_description',
        ),
        migrations.AlterField(
            model_name='complaint',
            name='request_image',
            field=models.ImageField(blank=True, null=True, upload_to='complaints'),
        ),
    ]
