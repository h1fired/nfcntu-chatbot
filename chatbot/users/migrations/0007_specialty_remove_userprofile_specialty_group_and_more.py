# Generated by Django 4.2.1 on 2023-05-29 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_userprofile_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='specialty',
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.specialty')),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.group', verbose_name='Група студента'),
        ),
    ]
