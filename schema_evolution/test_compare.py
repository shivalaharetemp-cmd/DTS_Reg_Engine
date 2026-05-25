from schema_evolution.compare import (
    compare_schemas
)

old_schema = {

    "tag": "LEDGER",

    "path": "/LEDGER",

    "datatype": "string",

    "attributes": {},

    "is_list": False,

    "children": [

        {
            "tag": "NAME",

            "path": "/LEDGER/NAME",

            "datatype": "string",

            "attributes": {},

            "is_list": False,

            "children": []
        }
    ]
}


new_schema = {

    "tag": "LEDGER",

    "path": "/LEDGER",

    "datatype": "string",

    "attributes": {},

    "is_list": False,

    "children": [

        {
            "tag": "NAME",

            "path": "/LEDGER/NAME",

            "datatype": "string",

            "attributes": {},

            "is_list": False,

            "children": []
        },

        {
            "tag": "GSTTYPE",

            "path": "/LEDGER/GSTTYPE",

            "datatype": "string",

            "attributes": {},

            "is_list": False,

            "children": []
        }
    ]
}

result = compare_schemas(
    old_schema,
    new_schema
)

print(result)