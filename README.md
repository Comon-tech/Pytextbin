# PyTextBin

<!-- ![image](https://github.com/Comon-tech/Pytextbin/assets/94454803/ab22455d-1b62-4749-908f-d4ac22f12f44)
-->
![pytextbin-transformed](https://github.com/Comon-tech/Pytextbin/assets/94454803/71f23858-6e7b-4527-b816-573ddf6f7cd6)

**PyTextBin** 
is a versatile Python library facilitating seamless conversion between text, binary, JSON, base64, xml and CSV formats with ease.'
See the [documentaion](https://github.com/Comon-tech/Pytextbin/) for more information


## Installation

You can install **PyTextBin** using pip from PyPI:

```bash
pip install PyTextBin
```

Alternatively, you can find the project on GitHub:

[GitHub Repository](https://github.com/C-o-m-o-n/PyTextBin)

## Usage

### Text and Binary

```python
# Import everything from textbin
from pytextbin import *

#To begin, create an object from the Textbin() class, which you'll use to access all the methods.


# 0) create textbin_obj instance 
textbin_obj = pytextbin.Textbin()

# 1) convert text to binary
text = 'hello world'
converted = textbin_obj.to_binary(text)
print("to_binary>>", converted)

# 2) convert json data to a base64 string
json_data = { 'id' : 12 , 'name' : 'Collins' }
converted = textbin_obj.json_to_base64(json_data)
print("json_to_base64>>", converted)

base64_data = 'eyJpZCI6IDEyLCAibmFtZSI6ICJDb2xsaW5zIn0='
converted = textbin_obj.base64_to_json(base64_data)
print("base64_to_json>>", converted)

```

## Contributions

Contributions to **PyTextBin** are welcome! You can find the project's GitHub repository and contribute to its development.

- [GitHub Repository](https://github.com/C-o-m-o-n/textbin)

## Contributors
- [Collins O. Odhiambo](https://github.com/C-o-m-o-n)
- [Nathaniel Handan](https://github.com/Tinny-Robot)
- [Pabitra Banerjee](https://github.com/PB2204)
- [Roldex Stark](https://github.com/r0ld3x)
- [Lyubomir Ternavskiy](https://github.com/LyubomirT)
- [comony](https://github.com/comony)

Your contributions are highly appreciated! We hope that **PyTextBin** proves helpful to you. Thank you for using it.

#### I hope it be of help to you thank you. [Collins O. Odhiambo](https://github.com/C-o-m-o-n)
