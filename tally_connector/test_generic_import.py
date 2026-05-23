from tally_connector.client import (
    import_object
)


payload = {

    "_attributes": {

        "NAME": "Generic Engine Ledger",

        "ACTION": "Create"
    },

    "NAME": "Generic Engine Ledger",

    "PARENT": "Sundry Debtors",

    "OPENINGBALANCE": "25000"
}


response = import_object(
    "LEDGER",
    payload
)

print(response)