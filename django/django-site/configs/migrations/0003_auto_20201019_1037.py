# Generated by Django 3.0.2 on 2020-10-19 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configs', '0002_auto_20201019_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('image', models.CharField(max_length=255)),
                ('t_value', models.CharField(max_length=255, verbose_name='T_VALUE')),
            ],
        ),
        migrations.AlterField(
            model_name='configuration',
            name='image',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='label',
            unique_together={('key', 'value')},
        ),
        migrations.DeleteModel(
            name='CustomConfig',
        ),
        migrations.AddField(
            model_name='service',
            name='labels',
            field=models.ManyToManyField(related_name='labels', to='configs.Label'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configs.Service'),
            preserve_default=False,
        ),
    ]
