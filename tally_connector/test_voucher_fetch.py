from tally_connector.fetch_voucher import (
    fetch_voucher
)

xml = fetch_voucher(
    "Sales",
    "1"
)

print(xml)