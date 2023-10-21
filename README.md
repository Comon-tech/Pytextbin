# textbin

**textbin** is a Python package that provides text-to-binary and binary-to-text conversion, as well as JSON-to-base64 and base64-to-JSON encoding and decoding.
See the [documentaion](https://c-o-m-o-n.github.io/textbin/) for more information


## Installation

You can install **textbin** using pip from PyPI:

```bash
pip install textbin
```

Alternatively, you can find the project on GitHub:

[GitHub Repository](https://github.com/C-o-m-o-n/textbin)

## Usage

### Text and Binary

```python
from textbin.textbin import *

# Convert text to binary
word = "hello"
converted_word = textbin.to_binary(word)
print(converted_word)  # Output: '1101000 1100101 1101100 1101100 1101111'

# Convert binary to text
binary = "1101000 1100101 1101100 1101100 1101111"
converted_binary = textbin.to_text(binary)
print(converted_binary)  # Output: hello
```

### JSON and Base64

```python
from textbin.textbin import json_to_base64, base64_to_json

# Encode a JSON object to base64
word = {"foo": "bar"}
converted_word = json_to_base64(word)
print(converted_word)  # Output: eyJmb28iOiAiYmFyIn0=

# Decode a base64 string to a JSON object
base64_string = "eyJmb28iOiAiYmFyIn0="
converted_binary = base64_to_json(base64_string)
print(converted_binary)  # Output: {'foo': 'bar'}
```

## Contributions

Contributions to **textbin** are welcome! You can find the project's GitHub repository and contribute to its development.

- [GitHub Repository](https://github.com/C-o-m-o-n/textbin)

## Contributors

- [Roldex](https://github.com/r0ld3x)

Your contributions are highly appreciated! We hope that **textbin** proves helpful to you. Thank you for using it.

#### I hope it be of help to you thank you. c-o-m-o-n
