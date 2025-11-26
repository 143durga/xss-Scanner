import random
import string

class PayloadGenerator:
    """
    Simple context-aware payload generator.
    Returns unique marker tokens easy to find in responses.
    """
    def __init__(self):
        pass

    def _rand(self, n=6):
        return ''.join(random.choices(string.ascii_uppercase+string.digits, k=n))

    def make(self, context):
        uid = self._rand()
        context = context.replace(' ', '-').upper()

        return f"INJ_{context}_{uid}"
