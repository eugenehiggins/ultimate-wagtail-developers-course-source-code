
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class InfoBlock(blocks.StaticBlock):
    class Meta:
        icon = 'info'
        template = '...'
        label = 'General Information'
        admin_text = 'This is an info block'

    title = blocks.CharBlock(required=True)
    text = blocks.TextBlock(required=True)


class FAQBlock(blocks.StructBlock):
    class Meta:
        icon = 'question'
        template = '...'
        label = 'frequently asked questions'
        admin_text = 'This is my FAQ block'

    question = blocks.CharBlock(required=True)
    answer = blocks.RichTextBlock(required=True, features=['bold', 'italic', 'link'])

class FAQListBlock(blocks.ListBlock):
    def __init__(self, child_block=None, **kwargs):
        if child_block is None:
            child_block = FAQBlock()
        super().__init__(child_block, **kwargs)

    class Meta:
        min_num = 1
        max_num = 5
        label = "frequently asked questions"
        # icon = 'info'
        # template = '...'


class TextBlock(blocks.TextBlock):

    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            help_text = "Enter the text for this block",
            max_length = 1000,
            min_length = 2,
            required = False,

        )

    class Meta:
        icon = 'edit'
        template = "..."


class CarouselBlock(blocks.StreamBlock):
    image = ImageChooserBlock()
    quotation = blocks.StructBlock(
        [
            ('text', blocks.TextBlock()),
            ('author', blocks.TextBlock()),
        ]
    )

    class Meta:
        icon = 'image'
        template = '...'
        label = 'Carousel'


class CallToActionBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(
        features=['bold', 'italic', 'link'],
        required=True,
    )
    page = blocks.PageChooserBlock()
    button_text = blocks.CharBlock(
        max_length=100,
        required=False,
    )

    class Meta:
        icon = 'pick'
        template = '...'
        label = 'Call to Action'
        admin_text = 'This is a call to action block'


class ImageBlock(ImageChooserBlock):
    class Meta:
        template = "blocks/image_block.html"
        group = "Standalone blocks"
