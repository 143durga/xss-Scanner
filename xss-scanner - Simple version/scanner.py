import requests
from bs4 import BeautifulSoup
from payloads import PayloadGenerator

class Scanner:
    def __init__(self, timeout=10):
        self.session = requests.Session()
        self.pg = PayloadGenerator()
        self.timeout = timeout
        self.results = []

    def _detect_substring(self, text, payload):
        idx = text.find(payload)
        if idx == -1:
            return None
        start = max(0, idx-50)
        end = min(len(text), idx+len(payload)+50)
        return text[start:end]

    def _detect_attribute_name(self, html_text, payload):
        soup = BeautifulSoup(html_text, 'html.parser')
        for tag in soup.find_all():
            for attr_name in list(tag.attrs.keys()):
                if payload in str(attr_name):
                    return f"<{tag.name} ... {attr_name}=...>"
        return None

    def scan_get(self, url, params, contexts):
        for p in list(params.keys()):
            for ctx in contexts:
                payload = self.pg.make(ctx)
                new_params = params.copy()
                new_params[p] = payload
                try:
                    r = self.session.get(url, params=new_params, timeout=self.timeout)
                except Exception as e:
                    continue
                # simple substring detection
                snippet = self._detect_substring(r.text, payload)
                # additional check for attribute-name context
                if not snippet and ctx == 'attribute-name':
                    an = self._detect_attribute_name(r.text, payload)
                    if an:
                        snippet = an
                if snippet:
                    self.results.append({
                        'method': 'GET',
                        'url': r.url,
                        'param': p,
                        'context': ctx,
                        'payload': payload,
                        'snippet': snippet
                    })

    def scan_post(self, url, data, contexts):
        for p in list(data.keys()):
            for ctx in contexts:
                payload = self.pg.make(ctx)
                new_data = data.copy()
                new_data[p] = payload
                try:
                    r = self.session.post(url, data=new_data, timeout=self.timeout)
                except Exception as e:
                    continue
                snippet = self._detect_substring(r.text, payload)
                if not snippet and ctx == 'attribute-name':
                    an = self._detect_attribute_name(r.text, payload)
                    if an:
                        snippet = an
                if snippet:
                    self.results.append({
                        'method': 'POST',
                        'url': r.url,
                        'param': p,
                        'context': ctx,
                        'payload': payload,
                        'snippet': snippet
                    })
