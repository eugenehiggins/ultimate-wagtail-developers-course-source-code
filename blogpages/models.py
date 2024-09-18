from django.core.exceptions import ValidationError
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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        # Get all the blog detail pages
        blog_detail_pages = BlogDetail.objects.live().public().descendant_of(self)
        context['blog_detail_pages'] = blog_detail_pages
        return context


class BlogDetail(Page):

    template = 'blogpages/blog_detail_page.html'
    #parent_page_types = ['blogpages.BlogIndex']
    subpage_types = []

    subtitle = models.CharField(max_length=100, blank=True)
    body = RichTextField(
        blank=True,
        features=['h2', 'h3', 'bold', 'italic', 'link', 'ol', 'ul', 'hr', 'document-link', 'image', 'embed','code','strikethrough']
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]

    def clean(self):
        super().clean()
        errors = {}

        if 'blog' in self.title.lower():
            errors['title'] = 'Blog cannot be in the title'

        if 'blog' in self.subtitle.lower():
            errors['subtitle'] = 'Blog cannot be in the subtitle'

        if 'blog' in self.slug.lower():
            errors['slug'] = 'Blog cannot be in the slug'

        if errors:
            raise ValidationError(errors)