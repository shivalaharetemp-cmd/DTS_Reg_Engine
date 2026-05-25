import requests


def fetch_voucher_list():

    xml_request = """
    <ENVELOPE>

        <HEADER>

            <VERSION>1</VERSION>

            <TALLYREQUEST>Export</TALLYREQUEST>

            <TYPE>Data</TYPE>

            <ID>Day Book</ID>

        </HEADER>

        <BODY>

            <DESC>

                <STATICVARIABLES>

                    <SVEXPORTFORMAT>
                        $$SysName:XML
                    </SVEXPORTFORMAT>

                </STATICVARIABLES>

                <FETCHLIST>

                    <FETCH>DATE</FETCH>

                    <FETCH>VOUCHERNUMBER</FETCH>

                    <FETCH>VOUCHERTYPENAME</FETCH>

                    <FETCH>MASTERID</FETCH>

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