from middleware_runtime.processor import (
    process_ledger
)

result = process_ledger(
    "Cash"
)

print("\nCANONICAL:\n")

print(
    result["canonical"]
)

print("\nSCHEMA ROOT:\n")

print(
    result["schema"]["tag"]
)