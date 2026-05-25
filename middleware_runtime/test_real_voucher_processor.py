from lxml import etree

from tally_connector.fetch_voucher_list import (
    fetch_voucher_list
)

from canonical_mapper.recursive_mapper import (
    recursive_map
)

from canonical_mapper.voucher_mapping import (
    VOUCHER_MAPPING
)

from middleware_runtime.processor import (
    clean_xml
)

from runtime_store.store_runtime import (
    save_runtime_document
)


# FETCH XML
xml = fetch_voucher_list()


# CLEAN XML
cleaned_xml = clean_xml(
    xml
)


# PARSE XML
root = etree.fromstring(
    cleaned_xml.encode()
)


# FIND FIRST VOUCHER
voucher = root.find(
    ".//VOUCHER"
)


# MAP TO CANONICAL
result = recursive_map(
    voucher,
    VOUCHER_MAPPING
)


print("\nCANONICAL:\n")

print(result)


# SAVE TO DATABASE
save_runtime_document(

    object_type="VOUCHER",

    object_name=result.get(
        "voucher_number"
    ),

    raw_xml=cleaned_xml,

    canonical_data=result
)


print("\nSAVED TO DATABASE\n")