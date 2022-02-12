# My Information
UID = 118428369
Last_Name = "Ibrahim"
First_Name = "Syed Mohammad"


def caesar_str_enc(plain_text: str, encryption_key: int) -> str:
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
    

def caesar_str_dec(cipher_text: str, decryption_key: int) -> str:
    """ 
        A Caesar Cipher decryption function which takes in a
        cipher text string and an integer key and returns the plain text string.
    """

    return caesar_str_enc(cipher_text, 26 - (decryption_key % 26))


if __name__ == '__main__':
    original_plain_str = 'hi 123 abc parse it  '

    # Encryption and Decryption - Test #1
    key = 12
    expected_enc_str = 'tu123mnobmdequf'.upper()
    expected_plain_str = 'HI123ABCPARSEIT'

    actual_enc_str = caesar_str_enc(original_plain_str, key)
    actual_dec_str = caesar_str_dec(actual_enc_str, key)
    print("Encrypted string: ", actual_enc_str)
    print("Decrypted string: ", actual_dec_str)

    assert expected_enc_str == actual_enc_str
    assert expected_plain_str == actual_dec_str

    # Encryption and Decryption - Test #2
    key = 51
    expected_enc_str = 'gh123zabozqrdhs'.upper()

    actual_enc_str = caesar_str_enc(original_plain_str, key)
    actual_dec_str = caesar_str_dec(actual_enc_str, key)
    print("Encrypted string: ", actual_enc_str)
    print("Decrypted string: ", actual_dec_str)

    assert expected_enc_str == actual_enc_str
    assert expected_plain_str == actual_dec_str

    # Encryption and Decryption - Test #3
    original_plain_str = 'A TEST SENTENCE'
    key = 2
    expected_enc_str = 'CVGUVUGPVGPEG'
    expected_plain_str = 'ATESTSENTENCE'

    actual_enc_str = caesar_str_enc(original_plain_str, key)
    actual_dec_str = caesar_str_dec(actual_enc_str, key)
    print("Encrypted string: ", actual_enc_str)
    print("Decrypted string: ", actual_dec_str)

    assert expected_enc_str == actual_enc_str
    assert expected_plain_str == actual_dec_str
