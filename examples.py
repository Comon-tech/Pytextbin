# Import everything from textbin
from textbin import *

"""
Inside the textbin.py, there is a 'Textbin()' class which has the methods:
- to_binary: Converts text to binary representation.
- to_text: Converts binary representation to text.
- json_to_base64: Converts a JSON object to a base64-encoded string.
- base64_to_json: Converts a base64-encoded string to a JSON object.
- csv_to_json: Converts a CSV string to a JSON object.
- json_to_csv: Converts a JSON object to a CSV string.
- xml_to_json: Converts an XML string to a JSON object.
- json_to_xml: Converts a JSON object to an XML string.
- xml_to_csv: Converts an XML string to a CSV file.
-----

To begin, create an object from the Textbin() class, which you'll use to access all the methods.
"""

# 0) create textbin_obj instance 
textbin_obj = textbin.Textbin()

# 1) convert text to binary
text = 'hello world'
converted = textbin_obj.to_binary(text)
print(converted)

# 2) convert json data to a base64 string
json_data = { 'id' : 12 , 'name' : 'Collins' }
converted = textbin_obj.json_to_base64(json_data)
print(converted)

base64_data = 'eyJpZCI6IDEyLCAibmFtZSI6ICJDb2xsaW5zIn0'
converted = textbin_obj.base64_to_json(base64_data)
print(converted)




