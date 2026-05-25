from django.db import models


class RuntimeDocument(models.Model):

    object_type = models.CharField(
        max_length=100
    )

    object_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    raw_xml = models.TextField()

    canonical_data = models.JSONField()

    schema_version = models.IntegerField(
        default=1
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )