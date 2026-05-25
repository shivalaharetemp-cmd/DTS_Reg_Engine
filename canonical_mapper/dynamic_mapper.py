def get_xml_value(
    element,
    xml_field
):

    print("\nCHECKING:", xml_field)

    # ATTRIBUTE
    if xml_field in element.attrib:

        print("FOUND ATTRIBUTE")

        return element.attrib.get(
            xml_field
        )

    # CHILD NODE
    child = element.find(
        xml_field
    )

    if child is not None:

        print("FOUND CHILD")

        return child.text

    print("NOT FOUND")

    return None


def dynamic_map(
    element,
    mapping
):

    canonical = {}

    print("\nELEMENT ATTRIBUTES:\n")

    print(element.attrib)

    for canonical_field, xml_field in mapping.items():

        print("\nCHECKING:", xml_field)

        value = get_xml_value(
            element,
            xml_field
        )

        print(
            canonical_field,
            value
        )

        if value is not None:

            canonical[
                canonical_field
            ] = value

    return canonical