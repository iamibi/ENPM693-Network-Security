from Homework_2_Solution import row_trans_enc, row_trans_dec

if __name__ == "__main__":
    original_plain_str = "hi 123 abc parse it  "

    # Encryption and Decryption - Test #1
    key = 12
    expected_enc_str = "tu123mnobmdequf".upper()
    expected_plain_str = "HI123ABCPARSEIT"

    actual_enc_str = caesar_str_enc(original_plain_str, key)
    actual_dec_str = caesar_str_dec(actual_enc_str, key)
    print("Encrypted string: ", actual_enc_str)
    print("Decrypted string: ", actual_dec_str)

    assert expected_enc_str == actual_enc_str
    assert expected_plain_str == actual_dec_str

    # Encryption and Decryption - Test #2
    key = 51
    expected_enc_str = "gh123zabozqrdhs".upper()

    actual_enc_str = caesar_str_enc(original_plain_str, key)
    actual_dec_str = caesar_str_dec(actual_enc_str, key)
    print("Encrypted string: ", actual_enc_str)
    print("Decrypted string: ", actual_dec_str)

    assert expected_enc_str == actual_enc_str
    assert expected_plain_str == actual_dec_str

    # Encryption and Decryption - Test #3
    original_plain_str = "A TEST SENTENCE"
    key = 2
    expected_enc_str = "CVGUVUGPVGPEG"
    expected_plain_str = "ATESTSENTENCE"

    actual_enc_str = caesar_str_enc(original_plain_str, key)
    actual_dec_str = caesar_str_dec(actual_enc_str, key)
    print("Encrypted string: ", actual_enc_str)
    print("Decrypted string: ", actual_dec_str)

    assert expected_enc_str == actual_enc_str
    assert expected_plain_str == actual_dec_str
