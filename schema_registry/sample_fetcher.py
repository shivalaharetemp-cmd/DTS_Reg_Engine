from tally_connector.services import TallyConnector


LEDGER_FETCH_XML = """
<ENVELOPE>

    <HEADER>
        <VERSION>1</VERSION>
        <TALLYREQUEST>EXPORT</TALLYREQUEST>
        <TYPE>OBJECT</TYPE>
        <SUBTYPE>Ledger</SUBTYPE>
        <ID TYPE="Name">Cash</ID>
    </HEADER>

    <BODY>

        <DESC>

            <STATICVARIABLES>
                <SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT>
            </STATICVARIABLES>

            <FETCHLIST>

                <FETCH>Name</FETCH>
                <FETCH>Parent</FETCH>
                <FETCH>OpeningBalance</FETCH>

            </FETCHLIST>

        </DESC>

    </BODY>

</ENVELOPE>
"""


def fetch_ledger_object():

    connector = TallyConnector()

    return connector.send_xml(
        LEDGER_FETCH_XML
    )