# Generated by Django 2.2.3 on 2019-07-30 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mozfest', '0004_mozfestprimarypage_use_wide_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='mozfesthomepage',
            name='cta_button_destination',
            field=models.CharField(default='/proposals', help_text='The URL for the page that the CTA button in the primary nav bar should redirect to', max_length=2048),
        ),
        migrations.AddField(
            model_name='mozfesthomepage',
            name='cta_button_label',
            field=models.CharField(default='Submit proposal', help_text='Label text for the CTA button in the primary nav bar', max_length=250),
        ),
    ]
