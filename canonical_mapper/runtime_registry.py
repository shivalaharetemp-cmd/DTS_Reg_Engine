from canonical_mapper.models import (
    CanonicalFieldMap
)


def get_mapping(
    object_type
):

    rows = CanonicalFieldMap.objects.filter(
        object_type=object_type
    )

    mapping = {}

    for row in rows:

        mapping[
            row.canonical_field
        ] = row.tally_field

    return mapping