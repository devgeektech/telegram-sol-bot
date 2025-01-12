from django.core.exceptions import ValidationError
from django.db import models
from model_utils.managers import QueryManager


class Date(models.Model):
    """
    Date/abstract class
    """

    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True,
    )

    class Meta:
        abstract = True
        ordering = ['-created']
class Common(Date):
    """
    Generic/abstract class
    """

    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'

    status = models.CharField(
        verbose_name='Status',
        choices=Status.choices,
        default=Status.PUBLISHED,
        max_length=50,
    )

    objects = models.Manager()
    drafted = QueryManager(status=Status.DRAFT)
    published = QueryManager(status=Status.PUBLISHED)
class Meta(Date.Meta):
        abstract = True