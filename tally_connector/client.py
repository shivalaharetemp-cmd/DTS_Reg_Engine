import requests

import xml.etree.ElementTree as ET

from xml_generator.builder import build_xml
from xml_generator.envelope import build_envelope


TALLY_URL = "http://localhost:9000"


def import_object(
    object_type,
    payload
):

    object_xml = build_xml(
        object_type,
        payload
    )

    envelope = build_envelope(
        object_xml
    )

    xml_string = ET.tostring(
        envelope,
        encoding="unicode"
    )

    response = requests.post(

        TALLY_URL,

        data=xml_string.encode("utf-8"),

        headers={
            "Content-Type": "application/xml"
        }
    )

    return response.text