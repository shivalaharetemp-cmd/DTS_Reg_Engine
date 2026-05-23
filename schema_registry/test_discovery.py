from lxml import etree

from schema_registry.sample_fetcher import (
    fetch_ledger_object
)

from schema_registry.discovery import (
    discover_schema
)

from schema_registry.store import (
    save_schema
)

from schema_registry.models import (
    TallyObjectType
)


xml = fetch_ledger_object()

root = etree.fromstring(
    xml.encode("utf-8")
)

schema = discover_schema(root)

object_type, _ = TallyObjectType.objects.get_or_create(
    name="Ledger"
)

save_schema(
    schema,
    object_type
)

print("DONE")