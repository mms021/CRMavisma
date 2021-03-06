# Generated by Django 3.0.4 on 2021-01-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRMmain', '0007_crm_positions'),
    ]

    operations = [
        migrations.AddField(
            model_name='crm_positions',
            name='diametr_vne',
            field=models.FloatField(blank=True, max_length=100, null=True, verbose_name='Внешний'),
        ),
        migrations.AddField(
            model_name='crm_positions',
            name='diametr_vnut',
            field=models.FloatField(blank=True, max_length=100, null=True, verbose_name='Внутненний'),
        ),
        migrations.AddField(
            model_name='crm_positions',
            name='dlinna_max',
            field=models.FloatField(blank=True, max_length=100, null=True, verbose_name='max'),
        ),
        migrations.AddField(
            model_name='crm_positions',
            name='dop_k_splavy',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Доп к сплаву'),
        ),
        migrations.AddField(
            model_name='crm_positions',
            name='kollitsh',
            field=models.FloatField(blank=True, max_length=100, null=True, verbose_name='Кол-во'),
        ),
        migrations.AddField(
            model_name='crm_positions',
            name='kollitsh_kg',
            field=models.FloatField(blank=True, max_length=100, null=True, verbose_name='Вес, кг'),
        ),
        migrations.AddField(
            model_name='crm_positions',
            name='naimenovanie_TPL',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Наименование ТПЛ'),
        ),
        migrations.AddField(
            model_name='crm_positions',
            name='shirina_max',
            field=models.FloatField(blank=True, max_length=100, null=True, verbose_name='max'),
        ),
        migrations.AddField(
            model_name='crm_positions',
            name='shirina_min',
            field=models.FloatField(blank=True, max_length=100, null=True, verbose_name='min'),
        ),
        migrations.AddField(
            model_name='crm_positions',
            name='tolshina',
            field=models.FloatField(blank=True, max_length=100, null=True, verbose_name='Толщина'),
        ),
        migrations.AlterField(
            model_name='crm_positions',
            name='izdelie',
            field=models.CharField(blank=True, choices=[('SLIT', 'Круглый пруток'), ('LIST', 'Билет'), ('ELIC', 'Слиток')], max_length=10, null=True, verbose_name='Форма изделий'),
        ),
    ]
