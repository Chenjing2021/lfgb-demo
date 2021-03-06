# Generated by Django 3.1.5 on 2021-03-21 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_websitereport'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmreport',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='overallreport',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='farmreport',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='overallreport',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
