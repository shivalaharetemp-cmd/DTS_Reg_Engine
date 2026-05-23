import xml.etree.ElementTree as ET

from xml_generator.builder import (
    build_xml
)

from xml_generator.envelope import (
    build_envelope
)


data = {

    "_attributes": {

        "NAME": "Middleware Test Ledger",

        "ACTION": "Create"
    },

    "PARENT": "Sundry Debtors",

    "OPENINGBALANCE": 15000
}


ledger_xml = build_xml(
    "LEDGER",
    data
)

envelope = build_envelope(
    ledger_xml
)

xml_string = ET.tostring(
    envelope,
    encoding="unicode"
)

print(xml_string)