from django.core.exceptions import ValidationError
from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import TextBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail.snippets.blocks import SnippetChooserBlock

from blocks import blocks as custom_blocks


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

        if request.GET.get('tag', None):
            tag = request.GET.get('tag')
            blog_detail_pages = blog_detail_pages.filter(tags__name=tag)
            context['tag'] = tag

        context['blog_detail_pages'] = blog_detail_pages
        return context

class BlogPageTags(TaggedItemBase):
    content_object = ParentalKey(
        'blogpages.BlogDetail',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class BlogDetail(Page):

    template = 'blogpages/blog_detail_page.html'

    tags = ClusterTaggableManager(through=BlogPageTags, blank=True)

    parent_page_types = ['blogpages.BlogIndex']
    subpage_types = []

    subtitle = models.CharField(max_length=100, blank=True)
    body = RichTextField(
        blank=True,
        features=['h2', 'h3', 'bold', 'italic', 'link', 'ol', 'ul', 'hr', 'document-link', 'image', 'embed','code','strikethrough']
    )

    body = StreamField(
        [
            ('text', custom_blocks.TextBlock()),
            ('info_block', custom_blocks.InfoBlock()),
            ('faq_block', custom_blocks.FAQListBlock()),
            ('image', custom_blocks.ImageBlock()),
            ('doc', DocumentChooserBlock()),
            ('page', blocks.PageChooserBlock(
                required=False,
                page_type='blogpages.BlogDetail',
            )),
            ('carousel', custom_blocks.CarouselBlock()),
            ('author', SnippetChooserBlock('blogpages.Author')),
            ('call_to_action', custom_blocks.CallToActionBlock()),
        ],
        block_counts={
            # 'text': {'min_num': 1},
            'image': {'max_num': 1},
        },
        use_json_field=True,
        blank=True,
        null=True,
    )


    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('subtitle'),

    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('tags'),
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