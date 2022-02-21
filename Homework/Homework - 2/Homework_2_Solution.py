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
    :param plain_text: str
    :param encryption_key: str
    :return: str
    """

    # Get the length of the key for adjusting the padding and number of columns
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
    pass


if __name__ == "__main__":
    enc_str = row_trans_enc("ATTACKPOSTPONEDUNTILTWOAM", "4312567")
    print("Encrypted string", enc_str)
