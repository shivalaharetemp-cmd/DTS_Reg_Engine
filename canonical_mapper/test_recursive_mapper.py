from lxml import etree

from canonical_mapper.recursive_mapper import (
    recursive_map
)


xml = """
<VOUCHER>

    <DATE>20260401</DATE>

    <VOUCHERNUMBER>2</VOUCHERNUMBER>

    <ALLLEDGERENTRIES.LIST>

        <LEDGERNAME>Cash</LEDGERNAME>

        <AMOUNT>-1000</AMOUNT>

    </ALLLEDGERENTRIES.LIST>

    <ALLLEDGERENTRIES.LIST>

        <LEDGERNAME>Sales</LEDGERNAME>

        <AMOUNT>1000</AMOUNT>

    </ALLLEDGERENTRIES.LIST>

</VOUCHER>
"""


root = etree.fromstring(
    xml.encode()
)


mapping = {

    "fields": {

        "voucher_date": {

            "field": "DATE",

            "lookup": "child"
        },

        "voucher_number": {

            "field": "VOUCHERNUMBER",

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
                }
            }
        }
    }
}


result = recursive_map(
    root,
    mapping
)

print(result)