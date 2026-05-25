from canonical_mapper.models import (
    CanonicalFieldMap
)


def seed_group_mapping():

    mappings = [

        {
            "canonical_field": "group_name",
            "tally_field": "NAME",
            "lookup_type": "attribute"
        },

        {
            "canonical_field": "parent",
            "tally_field": "PARENT",
            "lookup_type": "child"
        },

        {
            "canonical_field": "is_reserved",
            "tally_field": "ISSYSTEM",
            "lookup_type": "child"
        }
    ]

    for item in mappings:

        CanonicalFieldMap.objects.update_or_create(

            object_type="GROUP",

            canonical_field=item[
                "canonical_field"
            ],

            defaults={

                "tally_field": item[
                    "tally_field"
                ],

                "lookup_type": item[
                    "lookup_type"
                ]
            }
        )

    print("GROUP MAPPINGS SEEDED")