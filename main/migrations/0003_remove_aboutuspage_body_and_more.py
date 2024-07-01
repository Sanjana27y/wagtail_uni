# Generated by Django 5.0.6 on 2024-06-28 11:53

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_content_aboutuspage_body_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutuspage',
            name='body',
        ),
        migrations.RemoveField(
            model_name='aboutuspage',
            name='core_values',
        ),
        migrations.RemoveField(
            model_name='aboutuspage',
            name='intro',
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='content',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
