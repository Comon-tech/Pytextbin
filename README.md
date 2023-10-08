# textbin

#### textbin is a python package that converts text to binary and binary to text

# installation

> [pypi link](https://pypi.org/project/textbin/)
>
> > `pip install textbin`

> [git repo](https://github.com/C-o-m-o-n/textbin)

# usage

```python
from textbin.textbin import *

word = "hello"

converted_word = textbin.to_binary(word)

print(converted_word)

$ '1101000 1100101 1101100 1101100 1101111'


---

binary = "1101000 1100101 1101100 1101100 1101111"

converted_binary = textbin.to_binary(binary)

print(converted_binary)
$ hello

```

# JSON and Base64

```python
from textbin.textbin import json_to_base64,base64_to_base64

word = {"foo": "bar"}

converted_word = textbin.json_to_base64(word)

print(converted_word)  ## eyJmb28iOiAiYmFyIn0=

base64_string = "eyJmb28iOiAiYmFyIn0="

converted_binary = textbin.base64_to_base64(base64_string)

print(converted_binary)  ## {'foo': 'bar'}


```

# contributions

- [Roldex](https://github.com/r0ld3x)

### your contributions will be highly appreciated

#### I hope it be of help to you thank you. c-o-m-o-n
