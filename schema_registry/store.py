from schema_registry.models import (
    SchemaNode
)


def save_schema(
    schema,
    object_type
):

    SchemaNode.objects.update_or_create(

        object_type=object_type,

        path=schema["path"],

        defaults={

            "tag_name": schema["tag"],

            "datatype": schema["datatype"],

            "is_list": schema["is_list"],

            "attributes": schema["attributes"]
        }
    )

    for child in schema["children"]:

        save_schema(
            child,
            object_type
        )