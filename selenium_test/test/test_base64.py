import base64

test_str=base64.b64encode(b'admin:admin123456')
test_str2=base64.b64encode(b'binary\x00string')

print(test_str)
print(base64.b64decode(test_str).decode('utf-8'))
print(test_str2)