import requests

import xml.etree.ElementTree as ET

from xml_generator.builder import (
    build_xml
)

from xml_generator.envelope import (
    build_envelope
)


# DYNAMIC PAYLOAD

data = {

    "_attributes": {

        "NAME": "Middleware Test Ledger",

        "ACTION": "Create"
    },

    "NAME": "Middleware Test Ledger",

    "PARENT": "Sundry Debtors",

    "OPENINGBALANCE": "15000"
}


# GENERATE LEDGER XML

ledger_xml = build_xml(
    "LEDGER",
    data
)


# WRAP INSIDE ENVELOPE

envelope = build_envelope(
    ledger_xml
)


# CONVERT TO STRING

xml_string = ET.tostring(
    envelope,
    encoding="unicode"
)


print("\nSENDING XML:\n")

print(xml_string)


# SEND TO TALLY

response = requests.post(

    "http://localhost:9000",

    data=xml_string.encode("utf-8"),

    headers={
        "Content-Type": "application/xml"
    }
)


print("\nTALLY RESPONSE:\n")

print(response.text)