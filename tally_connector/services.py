import requests


class TallyConnector:

    def __init__(self, host="localhost", port=9000):

        self.url = f"http://{host}:{port}"

    def send_xml(self, xml):

        response = requests.post(
            self.url,
            data=xml.encode("utf-8")
        )

        return response.text