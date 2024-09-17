from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class BlogIndex(Page):

    template = 'blogpages/blog_index_page.html'
    #max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = ['blogpages.BlogDetail']

    subtitle = models.CharField(max_length=100, blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]


class BlogDetail(Page):

    template = 'blogpages/blog_detail_page.html'
    #parent_page_types = ['blogpages.BlogIndex']
    subpage_types = []

    subtitle = models.CharField(max_length=100, blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]
