import json
import base64


class Textbin:
    def to_binary(self, text):
        binary = " ".join(format(ord(i), "b") for i in str(text))
        return binary

    def to_text(self, binary):
        text = "".join(chr(int(i, 2)) for i in binary.split())
        return text

    def json_to_base64(self, json_data: dict or list):
        try:
            data = json.dumps(json_data)
        except Exception as e:
            print("[ERROR] Invalid json")
            return False
        base64_encoded = base64.b64encode(data.encode()).decode()
        return base64_encoded

    def base64_to_base64(self, base64_string: str):
        try:
            base64_decode = base64.b64decode(base64_string).decode()
        except Exception as e:
            print("[ERROR] Invalid json")
            return False
        json_data = json.loads(
            base64_decode,
        )
        return json_data


textbin = Textbin()
# print(textbin.json_to_base64({"hi": "hello"}))
# print(textbin.base64_to_base64("eyJoaSI6ICJoZWxsbyJ9=="))

word = {"foo": "bar"}

converted_word = textbin.json_to_base64(word)

print(converted_word)  ## eyJmb28iOiAiYmFyIn0=

base64_string = "eyJmb28iOiAiYmFyIn0="

converted_binary = textbin.base64_to_base64(base64_string)

print(converted_binary)  ## {'foo': 'bar'}
