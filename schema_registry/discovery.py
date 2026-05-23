from lxml import etree


def detect_type(element):

    type_attr = element.attrib.get("TYPE")

    if type_attr:
        return type_attr.lower()

    value = element.text

    if value is None:
        return "string"

    value = value.strip()

    if not value:
        return "string"

    try:
        int(value)
        return "integer"
    except:
        pass

    try:
        float(value)
        return "decimal"
    except:
        pass

    return "string"


def discover_schema(
    element,
    parent_path=""
):

    current_path = f"{parent_path}/{element.tag}"

    node = {
        "tag": element.tag,

        "path": current_path,

        "datatype": detect_type(element),

        "is_list": element.tag.endswith(".LIST"),

        "attributes": dict(element.attrib),

        "children": []
    }

    for child in element:

        child_schema = discover_schema(
            child,
            current_path
        )

        node["children"].append(
            child_schema
        )

    return node