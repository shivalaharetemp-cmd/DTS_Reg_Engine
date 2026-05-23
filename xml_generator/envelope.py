import xml.etree.ElementTree as ET


def build_envelope(object_xml):

    envelope = ET.Element("ENVELOPE")

    # =========================
    # HEADER
    # =========================

    header = ET.SubElement(
        envelope,
        "HEADER"
    )

    tally_request = ET.SubElement(
        header,
        "TALLYREQUEST"
    )

    tally_request.text = "Import Data"

    # =========================
    # BODY
    # =========================

    body = ET.SubElement(
        envelope,
        "BODY"
    )

    importdata = ET.SubElement(
        body,
        "IMPORTDATA"
    )

    # =========================
    # REQUEST DESC
    # =========================

    requestdesc = ET.SubElement(
        importdata,
        "REQUESTDESC"
    )

    reportname = ET.SubElement(
        requestdesc,
        "REPORTNAME"
    )

    reportname.text = "All Masters"

    staticvariables = ET.SubElement(
        requestdesc,
        "STATICVARIABLES"
    )

    svcompany = ET.SubElement(
        staticvariables,
        "SVCURRENTCOMPANY"
    )

    svcompany.text = "Tally Conection Test Company"

    # =========================
    # REQUEST DATA
    # =========================

    requestdata = ET.SubElement(
        importdata,
        "REQUESTDATA"
    )

    tallymessage = ET.SubElement(
        requestdata,
        "TALLYMESSAGE"
    )

    tallymessage.set(
        "xmlns:UDF",
        "TallyUDF"
    )

    tallymessage.append(object_xml)

    return envelope