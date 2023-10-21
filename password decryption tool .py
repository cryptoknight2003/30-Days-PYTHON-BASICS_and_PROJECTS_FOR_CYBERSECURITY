import base64
import binascii

encode_string = input("Enter the Base64 string: ")

try:
    decoded_password = base64.b64decode(encode_string).decode()
    print(f"Decoded password: {decoded_password}")
except (binascii.Error, UnicodeDecodeError) as e:
    print(f"Decoding error: {str(e)}")
