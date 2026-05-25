from lxml import etree


def extract_value(
    element,
    xml_field,
    lookup_type="child"
):

    # ATTRIBUTE LOOKUP
    if lookup_type == "attribute":

        value = element.attrib.get(
            xml_field
        )

        return value

    # CHILD LOOKUP
    child = element.find(
        xml_field
    )

    if child is not None:

        if child.text:

            return child.text.strip()

    return None


def map_simple_fields(
    element,
    field_mapping
):

    canonical = {}

    for canonical_field, config in field_mapping.items():

        xml_field = config.get(
            "field"
        )

        lookup_type = config.get(
            "lookup",
            "child"
        )

        value = extract_value(
            element,
            xml_field,
            lookup_type
        )

        if value is not None:

            canonical[
                canonical_field
            ] = value

    return canonical


def map_nested_list(
    element,
    list_tag,
    nested_mapping
):

    results = []

    list_elements = element.findall(
        list_tag
    )

    for item in list_elements:

        mapped_item = map_simple_fields(
            item,
            nested_mapping
        )

        if mapped_item:

            results.append(
                mapped_item
            )

    return results


def recursive_map(
    element,
    mapping
):

    canonical = {}

    #
    # SIMPLE FIELDS
    #
    simple_fields = mapping.get(
        "fields",
        {}
    )

    simple_result = map_simple_fields(
        element,
        simple_fields
    )

    canonical.update(
        simple_result
    )

    #
    # NESTED LISTS
    #
    nested_lists = mapping.get(
        "lists",
        {}
    )

    for canonical_list_name, list_config in nested_lists.items():

        xml_list_tag = list_config.get(
            "tag"
        )

        nested_mapping = list_config.get(
            "mapping",
            {}
        )

        mapped_list = map_nested_list(
            element,
            xml_list_tag,
            nested_mapping
        )

        canonical[
            canonical_list_name
        ] = mapped_list

    return canonical