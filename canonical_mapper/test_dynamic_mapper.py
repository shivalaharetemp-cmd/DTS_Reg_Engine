from lxml import etree

from canonical_mapper.registry import (
    LEDGER_MAPPING
)

from canonical_mapper.dynamic_mapper import (
    dynamic_map
)

xml_string = """
<LEDGER>

    <NAME>Cash</NAME>

    <PARENT>Cash-in-Hand</PARENT>

    <OPENINGBALANCE>
        15000
    </OPENINGBALANCE>

</LEDGER>
"""

root = etree.fromstring(
    xml_string
)

result = dynamic_map(
    root,
    LEDGER_MAPPING
)

print(result)