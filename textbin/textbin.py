import json
import base64
from typing import Union
import csv

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

    def csv_to_json(self, csv_string: str) -> Union[dict, list]:
        """Convert a CSV string to a JSON object."""
        try:
            csv_data = csv.reader(csv_string.splitlines())
            headers = next(csv_data)
            json_data = []
            for row in csv_data:
                row_dict = {}
                for i, value in enumerate(row):
                    row_dict[headers[i]] = value
                json_data.append(row_dict)
            return json_data
        except csv.Error as e:
            raise ValueError(f"Invalid CSV data: {e}")
        except Exception as e:
            raise ValueError(f"Error converting CSV to JSON: {e}")

    def json_to_csv(self, json_data: Union[dict, list]) -> str:
        """Convert a JSON object to a CSV string."""
        try:
            if isinstance(json_data, list) and len(json_data) > 0:
                headers = list(json_data[0].keys())
                csv_string = ",".join(headers) + "\n"
                for item in json_data:
                    csv_string += ",".join(str(item.get(header, "")) for header in headers) + "\n"
                return csv_string
            else:
                raise ValueError("JSON data must be a non-empty list of dictionaries")
        except Exception as e:
            raise ValueError(f"Error converting JSON to CSV: {e}")

    def csv_to_text(self, csv_string: str) -> str:
        """Convert a CSV string to plain text."""
        try:
            return csv_string
        except Exception as e:
            raise ValueError(f"Error converting CSV to text: {e}")

    def text_to_csv(self, text: str) -> str:
        """Convert plain text to a CSV string."""
        try:
            return text
        except Exception as e:
            raise ValueError(f"Error converting text to CSV: {e}")

    def csv_to_bin(self, csv_string: str) -> str:
        """Convert a CSV string to binary representation."""
        try:
            binary = self.to_binary(csv_string)
            return binary
        except Exception as e:
            raise ValueError(f"Error converting CSV to binary: {e}")

    def bin_to_csv(self, binary: str) -> str:
        """Convert binary representation to a CSV string."""
        try:
            csv_string = self.to_text(binary)
            return csv_string
        except Exception as e:
            raise ValueError(f"Error converting binary to CSV: {e}")

    def json_to_bin(self, json_data: Union[dict, list]) -> str:
        """Convert a JSON object to binary representation."""
        try:
            json_string = json.dumps(json_data)
            binary = self.to_binary(json_string)
            return binary
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data: {e}")
        except Exception as e:
            raise ValueError(f"Error converting JSON to binary: {e}")

    def bin_to_json(self, binary: str) -> Union[dict, list]:
        """Convert binary representation to a JSON object."""
        try:
            json_string = self.to_text(binary)
            json_data = json.loads(json_string)
            return json_data
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data: {e}")
        except Exception as e:
            raise ValueError(f"Error converting binary to JSON: {e}")

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
