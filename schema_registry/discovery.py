from lxml import etree


def detect_type(element):

    # PRIORITY 1:
    # Official Tally datatype from TYPE attribute
    type_attr = element.attrib.get("TYPE")

    if type_attr:

        return type_attr

    # PRIORITY 2:
    # Infer from text value

    value = element.text

    if value is None:
        return "string"

    value = value.strip()

    if not value:
        return "string"

    # INTEGER
    try:

        int(value)

        return "integer"

    except:
        pass

    # DECIMAL
    try:

        float(value)

        return "decimal"

    except:
        pass

    # BOOLEAN-LIKE
    lower_value = value.lower()

    if lower_value in [
        "yes",
        "no",
        "true",
        "false"
    ]:

        return "logical"

    # DEFAULT
    return "string"


def discover_schema(
    element,
    parent_path=""
):

    current_path = f"{parent_path}/{element.tag}"

    # ATTRIBUTE DISCOVERY
    attributes = dict(
        element.attrib
    )

    # LIST DETECTION
    is_list = False

    # Tally list naming convention
    if element.tag.endswith(".LIST"):

        is_list = True

    # Detect repeated child tags
    child_tags = [
        child.tag
        for child in element
    ]

    repeated_tags = set([
        tag
        for tag in child_tags
        if child_tags.count(tag) > 1
    ])

    node = {

        "tag": element.tag,

        "path": current_path,

        "datatype": detect_type(
            element
        ),

        "is_list": is_list,

        "attributes": attributes,

        "repeated_child_tags": list(
            repeated_tags
        ),

        "children": []
    }

    # RECURSIVE CHILD DISCOVERY
    for child in element:

        child_schema = discover_schema(
            child,
            current_path
        )

        node["children"].append(
            child_schema
        )

    return node