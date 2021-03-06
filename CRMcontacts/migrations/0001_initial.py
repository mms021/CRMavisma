# Generated by Django 3.0.4 on 2020-12-30 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CRM_Kompani',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CRM_Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('doljnost', models.CharField(blank=True, max_length=200, null=True)),
                ('tel_nomber', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('compani', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRMcontacts.CRM_Kompani')),
            ],
        ),
    ]
