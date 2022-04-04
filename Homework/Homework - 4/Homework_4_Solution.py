# Homework - 4 - Solution

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


# My Information
UID = 118428369
Last_Name = "Ibrahim"
First_Name = "Syed Mohammad"


# Global Constants
MAX_BLOCK_SIZE = 16


def aes_input_av_test(input_block, key, bit_list):
    """
    input_block and key are 16 byte long bytes values each
    bit_list is a list of integers that define the position of the
    bit in the input_block that needs to be inverted, one at a time, for example
    [0, 3, 6, 25, 78, 127]
    """

    # 1- any initializations necessary
    diff_list = []

    # 2- perform encryption of the original values
    original_cipher = aes_encrypt(input_block, key)

    # 3- for every value given in the bit_list:
    for position in bit_list:
        # invert the value of the corresponding bit in the input_block
        new_input = invert_bit(input_block, position)

        # perform encryption on the new input with one inverted bit at position b
        new_cipher = aes_encrypt(new_input, key)

        # find the number of bit differences between the two ciphertexts
        num_bit_differences = find_bit_difference(original_cipher, new_cipher)

        # add it to the list
        diff_list.append(num_bit_differences)

    # return the list of numbers
    return diff_list


def aes_key_av_test(input_block, key, bit_list):
    """
    input_block and key are 16 byte long bytes values each
    bit_list is a list of integers that define the position of the
    bit in the input_block that needs to be inverted, one at a time, for example
    [0, 3, 6, 25, 78, 127]
    """

    # 1- any initializations necessary
    diff_list = []

    # 2- perform encryption of the original values
    original_cipher = aes_encrypt(input_block, key)

    # 3- for every value given in the bitlist:
    for position in bit_list:
        # invert the value of the corresponding bit in the key
        new_key = invert_bit(key, position)

        # perform encryption with the new key with one inverted bit at position b
        new_cipher = aes_encrypt(input_block, new_key)

        # find the number of bit differences between the two ciphertexts
        num_bit_differences = find_bit_difference(original_cipher, new_cipher)

        # add it to the list
        diff_list.append(num_bit_differences)

    # return the list of numbers
    return diff_list


def invert_bit(input_val, position):
    """
    Inverts the bit of input_val at the given position value.

    :param input_val: bytes
    :param position: int
    """

    bits_list = list(convert_byte_to_bit_string(input_val))
    bits_list[position] = "0" if bits_list[position] == "1" else "1"
    bit_str = "".join(bits_list)
    return convert_bit_to_byte_string(bit_str)


def aes_encrypt(input_block, key):
    """
    Perform AES Encryption for the given input_block with the key provided.

    :param input_block: bytes
    :param key: bytes
    """

    # Make sure that the length of the input_block is MAX_BLOCK_SIZE long
    if len(input_block) < MAX_BLOCK_SIZE:
        input_block = pad(input_block, MAX_BLOCK_SIZE)

    # Set the mode to ECB
    mode = AES.MODE_ECB

    # Create the AES instance with the given key, mode and initialization vector
    aes_digest = AES.new(key=key, mode=mode)

    return aes_digest.encrypt(plaintext=input_block)


def find_bit_difference(value_1, value_2):
    """
    Get the number of bits changed between the original_val and new_val.

    :param value_1: bytes
    :param value_2: bytes
    """

    # Convert both the values to a bit list.
    val_1_bits = list(convert_byte_to_bit_string(value_1))
    val_2_bits = list(convert_byte_to_bit_string(value_2))

    difference = 0
    for index in range(len(val_1_bits)):
        if val_1_bits[index] != val_2_bits[index]:
            difference += 1

    return difference


def convert_byte_to_bit_string(input_bytes):
    return "".join(format(char, "08b") for char in input_bytes)


def convert_bit_to_byte_string(input_bits):
    str_list = []
    for index in range(0, len(input_bits), 8):
        char = chr(int(input_bits[index : index + 8], base=2))
        str_list.append(char)
    return "".join(str_list).encode(encoding="utf-8")
