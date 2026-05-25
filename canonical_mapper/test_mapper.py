from lxml import etree

from canonical_mapper.mappers import (
    map_ledger_from_tally
)

xml_string = """
<LEDGER>

    <NAME>Cash</NAME>

    <PARENT>Cash-in-Hand</PARENT>

    <OPENINGBALANCE>
        15000
    </OPENINGBALANCE>

    <ISBILLWISEON>
        Yes
    </ISBILLWISEON>

</LEDGER>
"""

root = etree.fromstring(
    xml_string
)

result = map_ledger_from_tally(
    root
)

print(result)