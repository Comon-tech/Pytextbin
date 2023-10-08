import json
import base64
from typing import Union

class Textbin:
    def to_binary(self, text: str) -> str:
        """Convert text to binary representation."""
        binary = " ".join(format(ord(i), "b") for i in str(text))
        return binary

    def to_text(self, binary: str) -> str:
        """Convert binary representation to text."""
        text = "".join(chr(int(i, 2)) for i in binary.split())
        return text

    def json_to_base64(self, json_data: Union[dict, list]) -> str:
        """Convert a JSON object to base64-encoded string."""
        try:
            data = json.dumps(json_data)
            base64_encoded = base64.b64encode(data.encode()).decode()
            return base64_encoded
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data: {e}")
        except Exception as e:
            raise ValueError(f"Error encoding to base64: {e}")

    def base64_to_json(self, base64_string: str) -> Union[dict, list]:
        """Convert a base64-encoded string to a JSON object."""
        try:
            base64_decode = base64.b64decode(base64_string).decode()
            json_data = json.loads(base64_decode)
            return json_data
        except base64.binascii.Error as e:
            raise ValueError(f"Invalid base64 data: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data: {e}")
        except Exception as e:
            raise ValueError(f"Error decoding from base64: {e}")

if __name__ == "__main__":
    textbin = Textbin()
    
    word = {"foo": "bar"}

    try:
        converted_word = textbin.json_to_base64(word)
        print(converted_word)  # Output: eyJmb28iOiAiYmFyIn0=
        
        base64_string = "eyJmb28iOiAiYmFyIn0="
        converted_binary = textbin.base64_to_json(base64_string)
        print(converted_binary)  # Output: {'foo': 'bar'}
    except ValueError as e:
        print(f"Error: {e}")
