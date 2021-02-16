# Generated by Django 3.0.4 on 2021-01-01 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRMcontacts', '0004_auto_20201231_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crm_kompani',
            name='sfera',
            field=models.CharField(blank=True, choices=[('AVI', 'Авиационный'), ('PRE', 'Предпиятие'), ('PRE', 'Энеретика')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='crm_kompani',
            name='tip',
            field=models.CharField(blank=True, choices=[('ПО', 'тип проек'), ('НДА', 'NDA')], max_length=10, null=True),
        ),
    ]