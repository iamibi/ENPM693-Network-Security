# Homework - 2
# Row Transposition Cipher
# Encryption and Decryption

from math import ceil

# My Information
UID = 118428369
Last_Name = "Ibrahim"
First_Name = "Syed Mohammad"


def row_trans_enc(plain_text, encryption_key):
    """
    Method to perform Row Transposition Cipher encryption using the plain_text
    and encryption_key provided.
    :param plain_text: str - Message to be encrypted
    :param encryption_key: str - The key used for encrypting the plain_text message
    :return: str - Cipher Text
    """

    # Get the length of the key for number of columns
    columns = len(encryption_key)

    # If the length of key is 0, return the plain_text string
    if columns == 0:
        return plain_text

    # Remove the spaces and other escape characters from the plain_text
    modified_text = plain_text.strip().replace(" ", "")

    # Get the number of rows for the matrix
    message_len = float(len(modified_text))
    rows = int(ceil(message_len / columns))

    # Apply padding to the plain_text
    padding_len = int((rows * columns) - message_len)
    padding_char = "X"
    modified_text += padding_char * padding_len

    # Build the matrix and perform insertion row by row from the modified_text
    # The slice condition for `for-in` loop is based on column size
    matrix = [
        modified_text[pt : pt + columns] for pt in range(0, len(modified_text), columns)
    ]

    # Convert the encryption_key to a list and sort them in ascending order
    encryption_key_list = sorted([int(val) for val in encryption_key])

    cipher_text = []
    for col in range(columns):
        # Get the index of the individual key value from sorted list of key
        current = encryption_key.index(str(encryption_key_list[col]))

        # Generate current_row from the matrix
        current_row = [row[current] for row in matrix]

        # Append the current_row to the final cipher_text list
        cipher_text.append("".join(current_row))

    return "".join(cipher_text)


def row_trans_dec(cipher_text, decryption_key):
    """
    Method to perform Row Transposition Cipher decryption using the cipher_text
    and decryption_key provided.
    :param cipher_text: str - Encrypted text to be decrypted
    :param decryption_key: str - The key that will be used to perform decryption on the cipher_text
    :return: str - Plain Text
    """

    # Get the length of the key for number of columns
    columns = len(decryption_key)

    # Get the number of rows for the matrix
    message_len = float(len(cipher_text))
    rows = int(ceil(message_len) / columns)

    # Generate an empty matrix to be filled
    # The generated matrix will look like [[None x columns], [None x columns], ... x rows]
    matrix = [[None] * columns for _ in range(rows)]

    # Convert the decryption_key to an integer list and sort them
    decryption_key_list = sorted(list([int(val) for val in decryption_key]))

    index = 0
    for col in range(columns):
        # Get the index of the individual key value from the original decryption_key
        current = decryption_key.index(str(decryption_key_list[col]))

        # Build a matrix from each of the cipher_text value at position `row`
        for row in range(rows):
            matrix[row][current] = cipher_text[index]
            index += 1

    # Convert the matrix to a string
    # The sum(matrix, []) will convert a list like this [['A', 'B'], ['C', 'D']] to
    # a list ['A', 'B', 'C', 'D']
    return "".join(sum(matrix, []))
