# from django.db import models
# from wagtail.models import Page
# from wagtail.admin.panels import FieldPanel
# from wagtail.fields import RichTextField, StreamField
# from wagtail.images.blocks import ImageChooserBlock
# from wagtail import blocks


# class HomePage(Page):
#     intro = RichTextField(blank=True)
#     slideshow_images = StreamField([
#         ('image', ImageChooserBlock())
#     ], blank=True)
#     important_points = StreamField([
#         ('point', blocks.CharBlock())
#     ], blank=True)

#     content_panels = Page.content_panels + [
#         FieldPanel('intro'),
#         FieldPanel('slideshow_images'),
#         FieldPanel('important_points'),
#     ]

# class AboutUsPage(Page):
#     content = RichTextField(blank=True)

#     content_panels = Page.content_panels + [
#         FieldPanel('content'),
#     ]

# class ContactUsPage(Page):
#     content = RichTextField(blank=True)

#     content_panels = Page.content_panels + [
#         FieldPanel('content'),
#     ]

# class FacultyPage(Page):
#     content = RichTextField(blank=True)

#     content_panels = Page.content_panels + [
#         FieldPanel('content'),
#     ]

# class CoursesPage(Page):
#     content = RichTextField(blank=True)

#     content_panels = Page.content_panels + [
#         FieldPanel('content'),
#     ]

# class GalleryPage(Page):
#     content = RichTextField(blank=True)

#     content_panels = Page.content_panels + [
#         FieldPanel('content'),
#     ]

# class AdmissionPage(Page):
#     content = RichTextField(blank=True)

#     content_panels = Page.content_panels + [
#         FieldPanel('content'),
#     ]
