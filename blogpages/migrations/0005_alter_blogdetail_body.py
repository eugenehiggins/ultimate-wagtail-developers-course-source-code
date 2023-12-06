# Generated by Django 4.2.5 on 2023-11-20 17:22

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("blogpages", "0004_blogdetail_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogdetail",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("text", wagtail.blocks.TextBlock()),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                    (
                        "carousel",
                        wagtail.blocks.StreamBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "quotation",
                                    wagtail.blocks.StructBlock(
                                        [
                                            ("text", wagtail.blocks.TextBlock()),
                                            ("author", wagtail.blocks.TextBlock()),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]