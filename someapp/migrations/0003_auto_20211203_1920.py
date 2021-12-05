# Generated by Django 3.2.9 on 2021-12-03 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('someapp', '0002_auto_20211203_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='SomeOtherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='somemodel',
            name='other',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='someapp.someothermodel'),
        ),
    ]
