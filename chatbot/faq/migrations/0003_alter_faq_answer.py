# Generated by Django 4.2.1 on 2023-06-11 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_faq_answer_faq_is_sent_alter_faq_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(blank=True, help_text='After submission, the answer field will not be editable.', max_length=2048, null=True),
        ),
    ]
