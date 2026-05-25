def map_ledger_from_tally(
    ledger_xml
):

    canonical = {

        "ledger_name": "",

        "parent": "",

        "opening_balance": 0,

        "is_billwise": False
    }

    for child in ledger_xml:

        tag = child.tag

        text = child.text

        if text:
            text = text.strip()

        if tag == "NAME":

            canonical["ledger_name"] = text

        elif tag == "PARENT":

            canonical["parent"] = text

        elif tag == "OPENINGBALANCE":

            canonical["opening_balance"] = text

        elif tag == "ISBILLWISEON":

            canonical["is_billwise"] = (
                text == "Yes"
            )

    return canonical