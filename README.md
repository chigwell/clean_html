[![PyPI version](https://badge.fury.io/py/clean_html.svg)](https://badge.fury.io/py/clean_html)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/clean_html)](https://pepy.tech/project/clean_html)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/eugene-evstafev-716669181/)

# clean_html

`clean_html` is a Python package designed for efficiently stripping HTML tags from strings while preserving character references.

## Installation

To install `clean_html`, use pip:

```bash
pip install clean_html
```

## Usage

Using `clean_html` is straightforward. Import the `strip_html` function and pass your HTML string to it.

```python
from clean_html import strip_html

html_content = "<p>This is <b>bold</b> text with an &amp; ampersand.</p>"
cleaned_text = strip_html(html_content)
print(cleaned_text)
```

This will output:

```
This is bold text with an & ampersand.
```

## Features

- Removes HTML tags from a given string.
- Preserves and correctly decodes HTML character references (e.g., `&amp;` becomes `&`).
- Simple and easy to use.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/chigwell/clean_html/issues).

## License

`clean_html` is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Author

**Eugene Evstafev**
<a href="https://www.linkedin.com/in/eugene-evstafev-716669181/"><img src="https://img.shields.io/badge/LinkedIn-blue" alt="LinkedIn"></a>

Repository: [https://github.com/chigwell/clean_html](https://github.com/chigwell/clean_html)