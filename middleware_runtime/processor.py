from lxml import etree
import re

from tally_connector.fetcher import (
    fetch_object
)

from schema_registry.discovery import (
    discover_schema
)

from schema_evolution.compare import (
    compare_schemas
)

from canonical_mapper.dynamic_mapper import (
    dynamic_map
)

from canonical_mapper.runtime_registry import (
    get_mapping
)

def clean_xml(xml_data):

    # REMOVE RAW INVALID CONTROL CHARS
    xml_data = re.sub(

        r"[\x00-\x08\x0B\x0C\x0E-\x1F]",

        "",

        xml_data
    )

    # REMOVE INVALID XML CHARACTER REFERENCES
    xml_data = re.sub(

        r"&#x?[0-8BCEF];",

        "",

        xml_data
    )

    # REMOVE DECIMAL XML CHAR REFS LIKE &#4;
    xml_data = re.sub(

        r"&#([0-8]|1[0-9]|2[0-9]|30|31);",

        "",

        xml_data
    )

    return xml_data


def process_ledger(
    ledger_name
):

    # FETCH XML
    xml_data = fetch_object(
        "Ledger",
        ledger_name
    )

    cleaned_xml = clean_xml(
        xml_data
    )

    root = etree.fromstring(
        cleaned_xml.encode()
    )

    print("\nROOT TAG:\n")

    print(root.tag)

    print("\nALL TAGS:\n")

    for elem in root.iter():

        print(elem.tag)

    # FIND REAL LEDGER NODE

    ledger = None

    for elem in root.iter():

        if (
            elem.tag == "LEDGER"
            and elem.attrib.get("NAME")
        ):

            ledger = elem

            break
    
    print("\nSELECTED LEDGER:\n")

    print(ledger.attrib)

    # DISCOVER SCHEMA
    schema = discover_schema(
        ledger
    )

    # MAP TO CANONICAL
    mapping = get_mapping(
        "LEDGER"
    )

    print("\nRUNTIME MAPPING:\n")

    print(mapping)

    canonical = dynamic_map(
        ledger,
        mapping
    )

    return {

        "schema": schema,

        "canonical": canonical
    }