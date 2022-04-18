# Homework - 5 - Solution

# Imports
from Crypto.Cipher import PKCS1_v1_5

# My Information
UID = 118428369
Last_Name = "Ibrahim"
First_Name = "Syed Mohammad"


def rsa_enc_public(plain_text, key_pair):
    """
        RSA Encryption for the given plain_text with the provided public key from the key_pair.

        plain_text - A given plain_text defined as a byte sequence.

        key_pair - A set of public and private key to be used for the process.

        :return: cipher_text, which is the encrypted data as byte sequence encrypted using the public key.
    """

    # Get the public key object from key_pair
    public_key = key_pair.public_key()

    # Initiate an encryptor_service to assist us in encrypting the message
    encryptor_service = PKCS1_v1_5.new(public_key)

    # Encrypt the input_block with RSA
    cipher_text = encryptor_service.encrypt(plain_text)

    return cipher_text


def rsa_dec_private(cipher_text, key_pair):
    """
        RSA Decryption for the given cipher_block with the provided private key from the key_pair.

        cipher_text - A given cipher_text defined as a byte sequence.

        key_pair - A set of public and private key to be used for the process.

        :return: plain_text, which is the decrypted data as byte sequence decrypted using the private key.
    """

    # Initialize the decryptor service from the private key
    decryptor_service = PKCS1_v1_5.new(key_pair)

    # Convert the cipher_text to plain_text using the decryptor_service
    plain_text = decryptor_service.decrypt(cipher_text, None)

    return plain_text
