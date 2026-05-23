from django.db import models

# Create your models here.
class TallyObjectType(models.Model):

    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)


class SchemaNode(models.Model):

    object_type = models.ForeignKey(
        TallyObjectType,
        on_delete=models.CASCADE
    )

    tag_name = models.CharField(
        max_length=255
    )

    path = models.TextField()

    datatype = models.CharField(
        max_length=50
    )

    is_list = models.BooleanField(
        default=False
    )

    attributes = models.JSONField(
        default=dict
    )

    class Meta:

        unique_together = (
            "object_type",
            "path"
        )


