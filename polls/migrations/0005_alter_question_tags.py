# Generated by Django 5.2.2 on 2025-07-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_tag_question_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='polls.tag'),
        ),
    ]
