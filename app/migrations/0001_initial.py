# Generated by Django 4.2.2 on 2023-06-30 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PBM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_sq_ft', models.IntegerField()),
                ('moisture', models.FloatField()),
                ('bag', models.IntegerField()),
                ('price', models.IntegerField()),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.commodity', verbose_name='Commodity FK')),
            ],
        ),
    ]
