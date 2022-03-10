from Homework_3_Solution import feistel_enc, feistel_dec


def validate(
    test_case: int,
    plain_text: str,
    rounds: int,
    seed: int,
    exp_enc_text_bytes: bytes,
    exp_dec_text_bytes: bytes,
) -> None:
    print(f"Testing Case #{test_case}")

    # Convert the string object to bytes string
    plain_text_bytes = plain_text.encode("utf-8")

    actual_enc_text_bytes = feistel_enc(plain_text_bytes, rounds, seed)
    actual_dec_text_bytes = feistel_dec(actual_enc_text_bytes, rounds, seed)

    print("Encrypted Text:", actual_enc_text_bytes)
    print("Decrypted Text:", actual_dec_text_bytes)

    assert exp_enc_text_bytes == actual_enc_text_bytes
    assert exp_dec_text_bytes == actual_dec_text_bytes


def test_homework():
    # Test Case - 1
    validate(
        test_case=1,
        plain_text="isthis16bytes?",
        rounds=16,
        seed=50,
        exp_enc_text_bytes=b"}\xd9\x93-G\x8e\xaa5\x95\x84\n\xb7q\xc4>\xb6",
        exp_dec_text_bytes=b"isthis16bytes?  "
    )

    # Test Case - 2
    validate(
        test_case=2,
        plain_text="testing123!",
        rounds=18,
        seed=44,
        exp_enc_text_bytes=b"\xa0|\xc8V\x1ec\xaf\xb7\xd8\xf1\xb0;\xc1^8\x90",
        exp_dec_text_bytes=b"testing123!     "
    )
