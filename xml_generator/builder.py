import xml.etree.ElementTree as ET


def build_xml(tag, data):

    element = ET.Element(tag)

    # HANDLE ATTRIBUTES

    attributes = data.get("_attributes", {})

    for attr_key, attr_value in attributes.items():

        element.set(
            attr_key,
            str(attr_value)
        )

    for key, value in data.items():

        # SKIP ATTRIBUTES NODE

        if key == "_attributes":
            continue

        # NESTED OBJECT

        if isinstance(value, dict):

            child = build_xml(
                key,
                value
            )

            element.append(child)

        # LIST HANDLING

        elif isinstance(value, list):

            list_element = ET.SubElement(
                element,
                key
            )

            for item in value:

                if isinstance(item, dict):

                    for sub_key, sub_value in item.items():

                        child = ET.SubElement(
                            list_element,
                            sub_key
                        )

                        child.text = str(sub_value)

                else:

                    child = ET.SubElement(
                        list_element,
                        "ITEM"
                    )

                    child.text = str(item)

        # NORMAL FIELD

        else:

            child = ET.SubElement(
                element,
                key
            )

            child.text = str(value)

    return element