from Homework_2_Solution import row_trans_enc, row_trans_dec


def validate(
    test_case: int,
    plain_text: str,
    cipher_key: str,
    exp_enc_text: str,
    exp_dec_text: str,
) -> None:
    print(f"Testing Case #{test_case}")
    actual_enc_text = row_trans_enc(plain_text, cipher_key)
    actual_dec_text = row_trans_dec(actual_enc_text, cipher_key)

    print("Encrypted Text:", actual_enc_text)
    print("Decrypted Text:", actual_dec_text)

    assert exp_enc_text == actual_enc_text
    assert exp_dec_text == actual_dec_text


if __name__ == "__main__":
    # Test Case - 1
    validate(
        test_case=1,
        plain_text="adguehislqid",
        cipher_key="3142",
        exp_enc_text="TTNAAPTMTSUOAODWCOIXKNLXPETX",
        exp_dec_text="ATTACKPOSTPONEDUNTILTWOAMXXX",
    )

    # Test Case - 2
    validate(
        test_case=2,
        plain_text="ATTACK POSTPONED UNTIL TWO AM",
        cipher_key="4312567",
        exp_enc_text="TTNAAPTMTSUOAODWCOIXKNLXPETX",
        exp_dec_text="ATTACKPOSTPONEDUNTILTWOAMXXX",
    )
    
    # Test Case - 3
    validate(
        test_case=3,
        plain_text="ATTACK postponed UNTIL TWO AM",
        cipher_key="4312567",
        exp_enc_text="TtNAApTMTsUOAodWCoIXKnLXpeTX",
        exp_dec_text="ATTACKpostponedUNTILTWOAMXXX",
    )
    
    # Test Case - 4
    validate(
        test_case=4,
        plain_text="MY NAME IS IBRAHIM",
        cipher_key="3261475",
        exp_enc_text="ARXYIXMSMMAXIIXNBXEHX",
        exp_dec_text="MYNAMEISIBRAHIMXXXXXX",
    )
