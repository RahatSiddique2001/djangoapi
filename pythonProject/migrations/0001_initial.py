# Generated by Django 4.2 on 2023-04-08 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200)),
                ('friendliness', models.IntegerField()),
                ('trainability', models.IntegerField()),
                ('shedding_amount', models.IntegerField()),
                ('excercise_needs', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('favourite_food', models.CharField(max_length=200)),
                ('favourite_toy', models.CharField(max_length=200)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dogs', to='pythonProject.breed')),
            ],
        ),
    ]
