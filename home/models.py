from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.images import get_image_model_string
from wagtail.models import Orderable, Page


class HomePage(Page):
    hero_title = models.CharField(max_length=255, blank=True)
    hero_tagline = models.TextField(blank=True)
    hero_button_text = models.CharField(max_length=100, blank=True)
    hero_button_link = models.CharField(max_length=255, blank=True)
    hero_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    about_heading = models.CharField(
        max_length=255,
        blank=True,
        default="About Bitesize Church",
    )
    about_text = RichTextField(blank=True)

    feature_heading = models.CharField(
        max_length=255,
        blank=True,
        default="Bitesize Brunch",
    )
    feature_text = RichTextField(blank=True)
    feature_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    events_heading = models.CharField(
        max_length=255,
        blank=True,
        default="Bitesize Brunch Dates",
    )
    events_intro = RichTextField(blank=True)

    location_heading = models.CharField(
        max_length=255,
        blank=True,
        default="Location",
    )
    location_text = RichTextField(blank=True)
    address = models.TextField(blank=True)
    directions_text = RichTextField(blank=True)
    parking_text = RichTextField(blank=True)
    map_url = models.URLField(blank=True)

    contact_heading = models.CharField(
        max_length=255,
        blank=True,
        default="Contact",
    )
    contact_text = RichTextField(blank=True)
    facebook_url = models.URLField(blank=True)
    contact_email = models.EmailField(blank=True)

    footer_text = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_tagline"),
        FieldPanel("hero_button_text"),
        FieldPanel("hero_button_link"),
        FieldPanel("hero_image"),
        FieldPanel("about_heading"),
        FieldPanel("about_text"),
        FieldPanel("feature_heading"),
        FieldPanel("feature_text"),
        FieldPanel("feature_image"),
        FieldPanel("events_heading"),
        FieldPanel("events_intro"),
        InlinePanel("brunch_dates", label="Brunch dates"),
        FieldPanel("location_heading"),
        FieldPanel("location_text"),
        FieldPanel("address"),
        FieldPanel("directions_text"),
        FieldPanel("parking_text"),
        FieldPanel("map_url"),
        FieldPanel("contact_heading"),
        FieldPanel("contact_text"),
        FieldPanel("facebook_url"),
        FieldPanel("contact_email"),
        FieldPanel("footer_text"),
    ]


class BrunchDate(Orderable):
    page = ParentalKey(
        "home.HomePage",
        related_name="brunch_dates",
        on_delete=models.CASCADE,
    )
    event_date = models.DateField()
    title = models.CharField(max_length=255, blank=True, default="Bitesize Brunch")
    note = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel("event_date"),
        FieldPanel("title"),
        FieldPanel("note"),
    ]

    def __str__(self):
        return f"{self.title} - {self.event_date}"