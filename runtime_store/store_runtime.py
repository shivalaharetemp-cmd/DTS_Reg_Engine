from runtime_store.models import (
    RuntimeDocument
)


def save_runtime_document(

    object_type,

    object_name,

    raw_xml,

    canonical_data
):

    RuntimeDocument.objects.create(

        object_type=object_type,

        object_name=object_name,

        raw_xml=raw_xml,

        canonical_data=canonical_data
    )