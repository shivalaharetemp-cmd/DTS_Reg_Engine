import requests


TALLY_URL = "http://localhost:9000"


def fetch_object(
    object_type,
    object_name
):

    xml_request = f"""
    <ENVELOPE>

        <HEADER>
            <VERSION>1</VERSION>
            <TALLYREQUEST>Export</TALLYREQUEST>
            <TYPE>Object</TYPE>
            <SUBTYPE>{object_type}</SUBTYPE>
            <ID TYPE="Name">{object_name}</ID>
        </HEADER>

        <BODY>

            <DESC>

                <STATICVARIABLES>

                    <SVEXPORTFORMAT>
                        $$SysName:XML
                    </SVEXPORTFORMAT>

                </STATICVARIABLES>

                <FETCHLIST>

                    <FETCH>*</FETCH>

                </FETCHLIST>

            </DESC>

        </BODY>

    </ENVELOPE>
    """

    response = requests.post(
        TALLY_URL,
        data=xml_request.encode("utf-8"),
        headers={
            "Content-Type": "application/xml"
        }
    )

    return response.text