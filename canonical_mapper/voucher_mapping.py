VOUCHER_MAPPING = {

    "fields": {

        "voucher_number": {

            "field": "VOUCHERNUMBER",

            "lookup": "child"
        },

        "voucher_type": {

            "field": "VOUCHERTYPENAME",

            "lookup": "child"
        },

        "voucher_date": {

            "field": "DATE",

            "lookup": "child"
        },

        "party_ledger": {

            "field": "PARTYLEDGERNAME",

            "lookup": "child"
        },

        "narration": {

            "field": "NARRATION",

            "lookup": "child"
        }
    },

    "lists": {

        "ledger_entries": {

            "tag": "ALLLEDGERENTRIES.LIST",

            "mapping": {

                "ledger_name": {

                    "field": "LEDGERNAME",

                    "lookup": "child"
                },

                "amount": {

                    "field": "AMOUNT",

                    "lookup": "child"
                },

                "is_party": {

                    "field": "ISPARTYLEDGER",

                    "lookup": "child"
                }
            }
        }
    }
}