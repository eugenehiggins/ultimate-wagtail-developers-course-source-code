from wagtail.images.formats import register_image_format, Format

register_image_format(
    Format('thumbnail', '150x150 thumbnail', 'richtext-image thumbnail-150', 'fill-150x150')
)