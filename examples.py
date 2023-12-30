# Import everything from textbin
from pytextbin import *

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
textbin_obj = pytextbin.Textbin()

# 1) convert text to binary
print("convert text to binary")
text = 'hello world'
converted = textbin_obj.to_binary(text)
print(converted)

print("************************************************************\n")

# 2) convert json data to a base64 string
print("convert json to base64")
json_data = { 'id' : 12 , 'name' : 'Collins' }
converted = textbin_obj.json_to_base64(json_data)
print(converted)

print("************************************************************\n")

# 3) convert base64 data to json
print("convert to base64 to json")
base64_data = 'eyJpZCI6IDEyLCAibmFtZSI6ICJDb2xsaW5zIn0='
converted = textbin_obj.base64_to_json(base64_data)
print(converted)

print("************************************************************\n")

#convert json to csv
print("convert json to csv")
json_list = [{ 'id' : 12 , 'name' : 'Collins' }]
converted = textbin_obj.json_to_csv(json_list)
print(converted)

print("************************************************************\n")


#convert json to xml
print("convert json to xml")
json_data = { 'id' : 12 , 'name' : 'Collins' }
converted = textbin_obj.json_to_xml(json_data)
print(converted)

print("************************************************************\n")

#convert xml to json
print("convert xml to json")
xml_data = "<item><id>12</id><name>Collins</name></item>"
converted = textbin_obj.xml_to_json(xml_data)
print(converted)

print("************************************************************\n")
