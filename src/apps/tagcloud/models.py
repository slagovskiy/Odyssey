from django.db import models


class Tag(models.Model):
    slug = models.SlugField(
        unique=True
    )
    name = models.CharField(
        max_length=255,
        default=''
    )
    deleted = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'