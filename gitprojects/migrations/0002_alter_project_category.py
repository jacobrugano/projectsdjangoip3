# Generated by Django 3.2.12 on 2022-04-11 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gitprojects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gitprojects.category'),
        ),
    ]