from html import unescape
from html.parser import HTMLParser

class _HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = []

    def handle_data(self, d):
        self.text.append(d)

    def get_data(self):
        return ''.join(self.text)

def strip_html(html_string: str) -> str:
    """
    Strips HTML tags from a string, preserving character references.

    Args:
        html_string: The string containing HTML.

    Returns:
        The string with HTML tags removed and character references unescaped.
    """
    stripper = _HTMLStripper()
    stripper.feed(html_string)
    return unescape(stripper.get_data())