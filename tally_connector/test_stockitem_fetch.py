from tally_connector.fetcher import (
    fetch_object
)

xml = fetch_object(
    "Stock Item",
    "Your Item Name"
)

print(xml)