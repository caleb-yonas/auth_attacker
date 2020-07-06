from urllib.parse import *
import urllib.parse
import base64

###url decoding the base64 string
url = unquote(input())
base64_string = url
print(base64_string)
###base64 decoding the string into raw text
base64_b = base64_string.encode("ascii")
sample_string_bytes = base64.b64decode(base64_b)
sample_string = sample_string_bytes.decode("ascii")
print(sample_string.replace('email@email.com', 'admin@libcurl.so'))

s_bytes = sample_string.encode('ascii')
base64_bytes = base64.b64encode(s_bytes)
base64_message = base64_bytes.decode('ascii')
final = urllib.parse.quote(base64_message)
print(f"Encoded, and replaced string: {final}")