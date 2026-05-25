from django.db import models


class CanonicalFieldMap(models.Model):

    object_type = models.CharField(
        max_length=100
    )

    canonical_field = models.CharField(
        max_length=100
    )

    tally_field = models.CharField(
        max_length=255
    )

    lookup_type = models.CharField(
        max_length=20,
        default="child"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )