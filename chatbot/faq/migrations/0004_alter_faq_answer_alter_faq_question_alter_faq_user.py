# Generated by Django 4.2.1 on 2023-06-11 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_userprofile_chat_id'),
        ('faq', '0003_alter_faq_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(blank=True, help_text='Note: After submission, the answer field will not be editable.', max_length=2048, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='faq',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
    ]
