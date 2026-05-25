from lxml import etree

from tally_connector.fetcher import (
    fetch_object
)

from schema_registry.discovery import (
    discover_schema
)

from canonical_mapper.dynamic_mapper import (
    dynamic_map
)

from canonical_mapper.runtime_registry import (
    get_mapping
)

from middleware_runtime.processor import (
    clean_xml
)


def process_object(
    object_type,
    object_name
):

    xml_data = fetch_object(
        object_type,
        object_name
    )

    cleaned_xml = clean_xml(
        xml_data
    )

    root = etree.fromstring(
        cleaned_xml.encode()
    )

    object_node = None

    for elem in root.iter():

        if (
            elem.tag.upper() == object_type.upper()
            and elem.attrib.get("NAME")
        ):

            object_node = elem

            break

    if object_node is None:

        raise Exception(
            f"{object_type} not found"
        )

    schema = discover_schema(
        object_node
    )

    mapping = get_mapping(
        object_type.upper()
    )

    canonical = dynamic_map(
        object_node,
        mapping
    )

    return {

        "schema": schema,

        "canonical": canonical
    }