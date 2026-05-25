def flatten_schema(
    schema,
    result=None
):

    if result is None:
        result = {}

    result[schema["path"]] = {

        "tag": schema["tag"],

        "datatype": schema["datatype"],

        "attributes": schema["attributes"],

        "is_list": schema["is_list"]
    }

    for child in schema["children"]:

        flatten_schema(
            child,
            result
        )

    return result


def compare_schemas(
    old_schema,
    new_schema
):

    old_flat = flatten_schema(
        old_schema
    )

    new_flat = flatten_schema(
        new_schema
    )

    old_paths = set(
        old_flat.keys()
    )

    new_paths = set(
        new_flat.keys()
    )

    added_fields = list(
        new_paths - old_paths
    )

    removed_fields = list(
        old_paths - new_paths
    )

    datatype_changes = []

    common_paths = old_paths.intersection(
        new_paths
    )

    for path in common_paths:

        old_type = old_flat[path]["datatype"]

        new_type = new_flat[path]["datatype"]

        if old_type != new_type:

            datatype_changes.append({

                "path": path,

                "old_type": old_type,

                "new_type": new_type
            })

    return {

        "added_fields": added_fields,

        "removed_fields": removed_fields,

        "datatype_changes": datatype_changes
    }