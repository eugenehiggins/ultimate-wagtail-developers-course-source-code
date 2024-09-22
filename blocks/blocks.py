from wagtail import blocks

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
        label = 'FAQ'
        admin_text = 'This is an FAQ block'

    question = blocks.CharBlock(required=True)
    answer = blocks.RichTextBlock(required=True, features=['bold', 'italic', 'link'])