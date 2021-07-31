from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from applications.core.models import Common, Seo


class Page(Common, Seo):
    title = models.CharField(max_length=225)
    slug = models.SlugField(max_length=40, unique=True)
    content = RichTextUploadingField()

