# Generated by Django 4.2.2 on 2023-06-30 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_pbm_commodity_delete_commodity'),
    ]

    operations = [
        migrations.CreateModel(
            name='PBPM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodity', models.CharField(max_length=50)),
                ('ft', models.IntegerField(verbose_name='FT')),
                ('rate', models.FloatField()),
                ('rent', models.IntegerField()),
                ('rent_per_mt', models.FloatField()),
                ('allway_space', models.IntegerField()),
                ('net_space', models.IntegerField()),
                ('bag_size', models.IntegerField()),
                ('space_per_bag', models.FloatField()),
                ('stack_ht', models.IntegerField()),
                ('utilisation', models.FloatField()),
                ('wh_capacity', models.FloatField()),
                ('value_per_bag', models.IntegerField()),
                ('whs', models.IntegerField()),
                ('whs_per_mt', models.FloatField()),
                ('sg', models.IntegerField()),
                ('sg_per_mt', models.FloatField()),
                ('other', models.IntegerField()),
                ('no_of_bag_utilization', models.IntegerField()),
                ('utilize_mt', models.IntegerField()),
                ('total_value', models.IntegerField()),
                ('insurance', models.IntegerField()),
                ('insurance_per_month', models.IntegerField()),
                ('insurance_per_mt', models.FloatField()),
                ('fumigation', models.IntegerField()),
                ('pmt', models.IntegerField()),
                ('fumigation_per_mt', models.IntegerField()),
                ('overhead_per_mt', models.IntegerField()),
                ('total_cost', models.IntegerField()),
                ('cost_per_bag', models.FloatField()),
                ('profit', models.FloatField()),
                ('base_rate_pbpm', models.FloatField()),
                ('base_rate_per_mt', models.FloatField()),
                ('profit_in_mt', models.FloatField()),
                ('base_rate_pmt', models.FloatField()),
                ('commodity_rate', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='PBM',
        ),
    ]
