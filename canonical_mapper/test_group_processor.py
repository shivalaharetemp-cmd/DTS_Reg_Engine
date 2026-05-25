from middleware_runtime.object_processor import (
    process_object
)

result = process_object(
    "GROUP",
    "Sundry Debtors"
)

print("\nCANONICAL:\n")

print(
    result["canonical"]
)

print("\nSCHEMA ROOT:\n")

print(
    result["schema"]["tag"]
)