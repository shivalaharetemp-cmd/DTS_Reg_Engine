from tally_connector.fetcher import (
    fetch_object
)


xml_data = fetch_object(

    "Ledger",

    "Cash"
)


print(xml_data)