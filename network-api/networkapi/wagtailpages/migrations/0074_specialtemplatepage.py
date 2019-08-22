# Generated by Django 2.2.4 on 2019-08-22 17:22

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtailmetadata.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailpages', '0073_indexpage_page_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialTemplatePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('template', models.CharField(blank=True, choices=[('unspecified', '-'), ('wagtailpages/one-off-pages/youtube.html', 'Youtube Campaign')], default='None', help_text='The template to be used to render this one-off page', max_length=500)),
                ('textfields', wagtail.core.fields.StreamField([('textblock', wagtail.core.blocks.StructBlock([('key', wagtail.core.blocks.CharBlock(help_text='the identifier to use in templates for fetching the text in this text block.', required=True)), ('textblock', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'link'], help_text='The page text that will be rendered into the page, using the associated key.'))]))])),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Search image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
    ]
