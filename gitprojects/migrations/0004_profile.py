# Generated by Django 4.0.4 on 2022-04-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gitprojects', '0003_project_dislikes_project_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
