import requests


def fetch_voucher(
    voucher_type,
    voucher_number
):

    xml_request = f"""
    <ENVELOPE>

        <HEADER>

            <VERSION>1</VERSION>

            <TALLYREQUEST>Export</TALLYREQUEST>

            <TYPE>Object</TYPE>

            <SUBTYPE>Voucher</SUBTYPE>

            <ID TYPE="Name">
                {voucher_number}
            </ID>

        </HEADER>

        <BODY>

            <DESC>

                <STATICVARIABLES>

                    <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>

                    <VoucherTypeName>
                        {voucher_type}
                    </VoucherTypeName>

                </STATICVARIABLES>

                <FETCHLIST>

                    <FETCH>*.*</FETCH>

                </FETCHLIST>

            </DESC>

        </BODY>

    </ENVELOPE>
    """

    response = requests.post(
        "http://localhost:9000",
        data=xml_request.encode(
            "utf-8"
        )
    )

    return response.text