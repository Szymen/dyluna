# Generated by Django 2.0 on 2017-12-21 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyluna_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='diet',
            field=models.ForeignKey(null=True, on_delete='CASCADE', to='dyluna_app.Diet'),
        ),
    ]
