# Generated by Django 5.0.6 on 2024-06-26 12:45

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutuspage',
            old_name='content',
            new_name='body',
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='core_values',
            field=wagtail.fields.StreamField([('core_value', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('description', wagtail.blocks.TextBlock(required=True))]))], blank=True),
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='intro',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
