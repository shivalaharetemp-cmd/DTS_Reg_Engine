from canonical_mapper.models import (
    CanonicalFieldMap
)


def seed_ledger_mapping():

    mappings = [

        {
            "canonical_field": "ledger_name",
            "tally_field": "NAME",
            "lookup_type": "attribute"
        },

        {
            "canonical_field": "parent",
            "tally_field": "PARENT",
            "lookup_type": "child"
        },

        {
            "canonical_field": "opening_balance",
            "tally_field": "OPENINGBALANCE",
            "lookup_type": "child"
        },

        {
            "canonical_field": "is_billwise",
            "tally_field": "ISBILLWISEON",
            "lookup_type": "child"
        }
    ]

    for item in mappings:

        CanonicalFieldMap.objects.update_or_create(

            object_type="LEDGER",

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

    print("LEDGER MAPPINGS SEEDED")