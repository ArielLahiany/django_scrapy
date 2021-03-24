# Django modules
from django.db import models


class StampedQuerySet(models.QuerySet):
    """
    Stamped query set manager.
    """

    pass


class Stamped(models.Model):
    """
    Stamped abstract model.
    """

    # Back-end fields.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Objects manager.
    objects = StampedQuerySet.as_manager()

    class Meta:
        abstract = True
        ordering = ["updated_at"]


class Quote(Stamped):
    """
    Quote initialization model.
    """

    # Back-end fields.
    quote = models.TextField()
    author = models.CharField(max_length=255)

    # Objects manager.
    objects = StampedQuerySet.as_manager()

    class Meta(Stamped.Meta):
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"

    def __str__(self):
        return self.quote
