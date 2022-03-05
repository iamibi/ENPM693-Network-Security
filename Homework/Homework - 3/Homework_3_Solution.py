# My Information
UID = 118428369
Last_Name = "Ibrahim"
First_Name = "Syed Mohammad"


def caesar_str_enc(plain_text, encryption_key):
    """ 
        A Caesar Cipher encryption function which takes in a
        plain text string and an integer key and returns a ciphered string.
    """
    
    # Make string uppercase
    updated_text = plain_text.upper()
    
    # Remove the spaces and escape characters from the string
    updated_text = updated_text.strip().replace(' ', '')

    # ASCII value of 'A'
    ascii_val = 65
    cipher_text = []
    for char in updated_text:
        cipher_char = char
        if char.isalpha():
            cipher_char = chr((ord(char) + encryption_key + ascii_val) % 26 + ascii_val)
        cipher_text.append(cipher_char)

    return ''.join(cipher_text)
    

def caesar_str_dec(cipher_text, decryption_key):
    """ 
        A Caesar Cipher decryption function which takes in a
        cipher text string and an integer key and returns the plain text string.
    """

    return caesar_str_enc(cipher_text, 26 - (decryption_key % 26))
