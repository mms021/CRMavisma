# Generated by Django 3.0.4 on 2021-01-18 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRMmain', '0020_auto_20210118_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='crm_p_postavka',
            name='data_sdad',
            field=models.DateField(blank=True, max_length=100, null=True),
        ),
    ]
