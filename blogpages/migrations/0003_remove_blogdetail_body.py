# Generated by Django 4.2.5 on 2023-11-16 17:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blogpages", "0002_blogpagetags_blogdetail_tags"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogdetail",
            name="body",
        ),
    ]
