# Generated by Django 3.0.2 on 2020-10-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configs', '0003_auto_20201019_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='t_value',
        ),
        migrations.AddField(
            model_name='service',
            name='t_version',
            field=models.CharField(default='blue', max_length=255, verbose_name='T_VERSION'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.CharField(default='gcr.io/knative-samples/knative-route-demo:blue', max_length=255),
        ),
    ]