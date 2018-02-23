# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answer', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CropPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CropName', models.CharField(max_length=20)),
                ('Price', models.FloatField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Relation', models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Son', 'Son'), ('Daughter', 'Daughter'), ('Wife', 'Wife'), ('Husband', 'Husband'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Other', 'Other')], max_length=20)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, verbose_name='Gender')),
                ('D_o_b', models.DateField(null=True)),
                ('Photo', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('Audio', models.FileField(max_length=200, upload_to='mp3/')),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lat_1', models.FloatField()),
                ('Long_1', models.FloatField()),
                ('Lat_2', models.FloatField()),
                ('Long_2', models.FloatField()),
                ('Lat_3', models.FloatField()),
                ('Long_3', models.FloatField()),
                ('Lat_4', models.FloatField()),
                ('Long_4', models.FloatField()),
                ('Season', models.CharField(choices=[('Karif', 'Karif'), ('Rabi', 'Rabi'), ('zaid', 'zaid')], max_length=50, verbose_name='Season')),
                ('Crop', models.CharField(choices=[('Rice', 'Rice'), ('Jowar', 'Jowar'), ('Bajra', 'Bajra'), ('Maize', 'Maize'), ('Ragi', 'Ragi'), ('Small Millets', 'Small Millets'), ('Pulses', 'Pulses'), ('Castor', 'Castor'), ('Tobacco', 'Tobacco'), ('Cotton', 'Cotton'), ('Sugarcane', 'Sugarcane')], max_length=50, verbose_name='Crop')),
                ('Farm_pic', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('Audio', models.FileField(max_length=200, upload_to='mp3/')),
            ],
        ),
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FertilizerName', models.CharField(max_length=20)),
                ('Price', models.FloatField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Kissan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=30)),
                ('Last_name', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=50)),
                ('Phone', models.IntegerField()),
                ('No_of_acres', models.IntegerField()),
                ('H_no', models.CharField(max_length=50)),
                ('Village', models.CharField(max_length=50)),
                ('District', models.CharField(choices=[('Ananthapur', 'Ananthapur'), ('Chittoor', 'Chittoor'), ('Karimnagar', 'Karimnagar'), ('East Godavari', 'East Godavari'), ('Guntur', 'Guntur'), ('Kadapa', 'Kadapa'), ('Krishna', 'Krishna'), ('Kurnool', 'Kurnool'), ('Nellore', 'Nellore'), ('Prakasam', 'Prakasam'), ('Srikakulam', 'Srikakulam'), ('Visakhapatnam', 'Visakhapatnam'), ('Vijayanagaram', 'Vijayanagaram'), ('West Godavari', 'West Godavari')], max_length=50)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, verbose_name='Gender')),
                ('D_o_b', models.DateField(null=True)),
                ('Total_monthly_income', models.IntegerField()),
                ('Profile_pic', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('Audio', models.FileField(max_length=200, upload_to='mp3/')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.TextField(max_length=100)),
                ('F_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jaikissan.Kissan')),
            ],
        ),
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SeedName', models.CharField(max_length=20)),
                ('Price', models.FloatField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lat', models.FloatField()),
                ('Long', models.FloatField()),
                ('Depth', models.FloatField()),
                ('Avg_water', models.FloatField()),
                ('Well_pic', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('Audio', models.FileField(max_length=200, upload_to='mp3/')),
                ('FF_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jaikissan.Farm')),
            ],
        ),
        migrations.CreateModel(
            name='WellUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(null=True)),
                ('Water_Yeild', models.FloatField()),
                ('Wellupadte_pic', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
                ('Audio', models.FileField(max_length=200, upload_to='mp3/')),
                ('W_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jaikissan.Well')),
            ],
        ),
        migrations.AddField(
            model_name='farm',
            name='F_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jaikissan.Kissan'),
        ),
        migrations.AddField(
            model_name='familymember',
            name='F_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jaikissan.Kissan'),
        ),
        migrations.AddField(
            model_name='answer',
            name='F_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jaikissan.Kissan'),
        ),
        migrations.AddField(
            model_name='answer',
            name='Q_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jaikissan.Question'),
        ),
    ]
