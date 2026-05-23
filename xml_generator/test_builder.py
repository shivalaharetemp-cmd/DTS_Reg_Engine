import xml.etree.ElementTree as ET

from xml_generator.builder import (
    build_xml
)


data = {

    "NAME": "ABC Traders",

    "PARENT": "Sundry Debtors",

    "OPENINGBALANCE": 1000,

    "ADDRESS.LIST": [

        {
            "ADDRESS": "Delhi"
        },

        {
            "ADDRESS": "Mumbai"
        }
    ]
}


xml_element = build_xml(
    "LEDGER",
    data
)

xml_string = ET.tostring(
    xml_element,
    encoding="unicode"
)

print(xml_string)