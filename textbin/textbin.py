import json
import base64
from typing import Union
import csv
import xml.etree.ElementTree as ET

class Textbin:
    """
    A class for converting between various text formats.

    Methods:
    - to_binary: Converts text to binary representation.
    - to_text: Converts binary representation to text.
    - json_to_base64: Converts a JSON object to a base64-encoded string.
    - base64_to_json: Converts a base64-encoded string to a JSON object.
    - xml_to_json: Converts an XML string to a JSON object.
    - json_to_xml: Converts a JSON object to an XML string.
    - xml_to_csv: Converts an XML string to a CSV file.
    """
    def __init__(self):
        pass

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


    def xml_to_json(self, xml_string: str) -> Union[dict, list]:
        """Convert an XML string to a JSON object."""
        try:
            root = ET.fromstring(xml_string)
            json_data = self._element_to_dict(root)
            return json_data
        except ET.ParseError as e:
            raise ValueError(f"Invalid XML data: {e}")
        except Exception as e:
            raise ValueError(f"Error converting from XML to JSON: {e}")

    def json_to_xml(self, json_data: Union[dict, list]) -> str:
        """Convert a JSON object to an XML string."""
        try:
            root = self._dict_to_element(json_data)
            xml_string = ET.tostring(root, encoding="unicode")
            return xml_string
        except Exception as e:
            raise ValueError(f"Error converting from JSON to XML: {e}")

    def xml_to_csv(self, xml_string: str, csv_file: str) -> None:
        """Convert an XML string to a CSV file."""
        try:
            root = ET.fromstring(xml_string)
            with open(csv_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                header = []
                for child in root:
                    row = []
                    for key, value in child.attrib.items():
                        if key not in header:
                            header.append(key)
                        row.append(value)
                    writer.writerow(row)
                writer.writerow(header)
        except ET.ParseError as e:
            raise ValueError(f"Invalid XML data: {e}") from e
        except Exception as e:
            raise ValueError(f"Error converting from XML to CSV: {e}") from e


    def _element_to_dict(self, element: ET.Element) -> Union[dict, list]:
        """Convert an ElementTree element to a dictionary."""
        if element:
            if element.attrib:
                return {element.tag: element.attrib}
            children = element.getchildren()
            if children:
                out = {}
                for child in children:
                    result = self._element_to_dict(child)
                    if child.tag in out:
                        if isinstance(out[child.tag], list):
                            out[child.tag].append(result)
                        else:
                            out[child.tag] = [out[child.tag], result]
                    else:
                        out[child.tag] = result
                return {element.tag: out}
            return {element.tag: element.text}
        return None

    def _dict_to_element(self, data: Union[dict, list]) -> ET.Element:
        """Convert a dictionary to an ElementTree element."""
        if isinstance(data, dict):
            items = data.items()
        elif isinstance(data, list):
            items = enumerate(data)
        else:
            raise ValueError(f"Invalid data type: {type(data)}")
        elem = ET.Element("item")
        for key, value in items:
            if isinstance(value, dict):
                child = self._dict_to_element(value)
                child.tag = key
                elem.append(child)
            elif isinstance(value, list):
                for item in value:
                    child = self._dict_to_element(item)
                    child.tag = key
                    elem.append(child)
            else:
                child = ET.Element(key)
                child.text = str(value)
                elem.append(child)
        return elem

if __name__ == "__main__":
    textbin = Textbin() 
    word = {"foo": "bar"}

    try:
        converted_word = textbin.json_to_base64(word)
        print(converted_word)  # Output: eyJmb28iOiAiYmFyIn0=     
        BASE64_STRING = "eyJmb28iOiAiYmFyIn0="
        converted_binary = textbin.base64_to_json(BASE64_STRING)
        print(converted_binary)  # Output: {'foo': 'bar'}
        
    except ValueError as e:
        print(f"Error: {e}")
