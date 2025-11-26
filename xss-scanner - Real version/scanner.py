import requests
from payloads import PayloadGenerator

class XSSScanner:
    def __init__(self):
        self.payloads = PayloadGenerator()

    def scan(self, url, params, method="GET", context="text"):
        results = []

        for param in params:
            for payload in self.payloads.for_context(context):
                data = {param: payload}

                if method == "GET":
                    resp = requests.get(url, params=data)
                else:
                    resp = requests.post(url, data=data)

                if payload in resp.text:  
                    snippet_index = resp.text.find(payload)
                    snippet = resp.text[max(0, snippet_index-40): snippet_index+40]

                    results.append({
                        "method": method,
                        "url": url,
                        "param": param,
                        "context": context,
                        "payload": payload,
                        "snippet": snippet
                    })

        return results
