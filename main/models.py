from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail import blocks
from wagtail.blocks import StructBlock, CharBlock, TextBlock
from wagtail.models import Orderable
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import InlinePanel
from wagtail.snippets.models import register_snippet

class CoreValueBlock(StructBlock):
    title = CharBlock(required=True)
    description = TextBlock(required=True)

    class Meta:
        template = "blocks/core_value_block.html"

class AboutUsPage(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)
    core_values = StreamField([('core_value', CoreValueBlock())], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('core_values'),
    ]

class MenuItem(Orderable):
    link_title = models.CharField(max_length=50)
    link_page = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name='+', on_delete=models.CASCADE)

    panels = [
        FieldPanel('link_title'),
        PageChooserPanel('link_page'),
    ]

    def __str__(self):
        return self.link_title

@register_snippet
class Menu(ClusterableModel):
    title = models.CharField(max_length=100)
    menu_items = models.ManyToManyField(MenuItem, related_name='menus', blank=True)

    panels = [
        FieldPanel('title'),
        InlinePanel('menu_items', label="Menu Items")
    ]

    def __str__(self):
        return self.title



class HomePage(Page):
    intro = RichTextField(blank=True)

    slideshow_images = StreamField([
        ('image', ImageChooserBlock())
    ], blank=True)
    important_points = StreamField([
        ('point', blocks.CharBlock())
    ], blank=True)
    # slideshow_images= models.ForeignKey(
    #     'wagttailimages.Image',
    #     null = True,
    #     blank = True,
    #     on_delete= models.SET_NULL,
    #     related_name = '+',
    # )

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('slideshow_images'),
        FieldPanel('important_points'),
    ]

class CoreValueBlock(StructBlock):
    title = CharBlock(required=True)
    description = TextBlock(required=True)

    class Meta:
        template = "blocks/core_value_block.html"


class ContactUsPage(Page):
    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]

class FacultyPage(Page):
    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]

class CoursesPage(Page):
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
