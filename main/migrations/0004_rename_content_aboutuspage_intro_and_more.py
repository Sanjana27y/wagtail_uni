# Generated by Django 5.0.6 on 2024-06-28 12:45

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_aboutuspage_body_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutuspage',
            old_name='content',
            new_name='intro',
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='campus_map',
            field=wagtail.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='core_values',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock())], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='history',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock())], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='research',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock())], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutuspage',
            name='vision_mission',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock())], blank=True, null=True),
        ),
    ]
