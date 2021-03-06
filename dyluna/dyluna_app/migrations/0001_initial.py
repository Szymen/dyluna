# Generated by Django 2.0 on 2018-01-23 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('menu', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('diet', models.ForeignKey(null=True, on_delete='CASCADE', to='dyluna_app.Diet')),
            ],
        ),
        migrations.CreateModel(
            name='User_Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('equipment', models.ForeignKey(null=True, on_delete='CASCADE', to='dyluna_app.Equipment')),
                ('type', models.ForeignKey(on_delete='CASCADE', to='dyluna_app.Type')),
                ('user', models.ForeignKey(on_delete='CASCADE', to='dyluna_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Workshop_Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('places', models.ManyToManyField(to='dyluna_app.Place')),
                ('workshop', models.ForeignKey(on_delete='CASCADE', to='dyluna_app.Workshop')),
            ],
        ),
        migrations.CreateModel(
            name='Meal_Time',
            fields=[
                ('meal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dyluna_app.Meal')),
                ('meal_time', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_role',
            field=models.ForeignKey(on_delete='CASCADE', to='dyluna_app.User_Role'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='user',
            field=models.ForeignKey(on_delete='CASCADE', to='dyluna_app.User'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='workshop',
            field=models.ForeignKey(on_delete='CASCADE', to='dyluna_app.Workshop'),
        ),
    ]
