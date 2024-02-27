def caesar_encode(plain_text, shift):
    cipher_text=""
    for i in plain_text:
        i_encoded = ord(i) + shift
        i_encoded = chr(i_encoded)
        cipher_text+=i_encoded
    return cipher_text
    