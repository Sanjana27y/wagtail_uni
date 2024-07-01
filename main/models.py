from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks
from wagtail.blocks import StructBlock, CharBlock, TextBlock, RichTextBlock
from wagtail.models import Orderable
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import InlinePanel
from wagtail.snippets.models import register_snippet
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock


class HomePage(Page):
    intro = RichTextField(blank=True)

    slideshow_images = StreamField([
        ('image', ImageChooserBlock())
    ], blank=True)
    important_points = StreamField([
        ('point', blocks.CharBlock())
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('slideshow_images'),
        FieldPanel('important_points'),
    ]


class AboutUsPage(Page):
    intro = RichTextField(blank=True)
    vision_mission = StreamField(
        [('paragraph', blocks.RichTextBlock())], null=True, blank=True)
    history = StreamField(
        [('paragraph', blocks.RichTextBlock())], null=True, blank=True)
    core_values = StreamField(
        [('paragraph', blocks.RichTextBlock())], null=True, blank=True)
    research = StreamField(
        [('paragraph', blocks.RichTextBlock())], null=True, blank=True)
    campus_map = StreamField(
        [('image', ImageChooserBlock())], null=True, blank=True)
  
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('vision_mission'),
        FieldPanel('history'),
        FieldPanel('core_values'),
        FieldPanel('research'),
        FieldPanel('campus_map'),
    ]

class CoursesPage(Page):
    intro = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        InlinePanel('courses', label="Courses"),
    ]

class Course(Orderable):
    page = ParentalKey('main.CoursesPage', on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    pdf = models.ForeignKey(
        'wagtaildocs.Document', on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('image'),
        FieldPanel('pdf'),
    ]


class FacultyPage(Page):
    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]



class GalleryPage(Page):
    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]

class AdmissionPage(Page):
    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]
