# Generated by Django 3.0.8 on 2021-10-10 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0006_bleeding_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bleeding',
            name='category',
        ),
        migrations.RemoveField(
            model_name='bleeding',
            name='name',
        ),
        migrations.AddField(
            model_name='bleeding',
            name='Trackable',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='tracking.Trackable'),
            preserve_default=False,
        ),
    ]
