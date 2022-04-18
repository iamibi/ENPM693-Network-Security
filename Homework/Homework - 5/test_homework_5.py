# test_homework_5.py

# Imports
from Homework_5_Solution import rsa_enc_public, rsa_dec_private
from Crypto.PublicKey import RSA
from unittest import TestCase


class TestHomework5(TestCase):
    def setUp(self) -> None:
        self.key_pair = RSA.generate(2048)

    def tearDown(self) -> None:
        self.key_pair = None

    def test_rsa_enc_public_valid(self):
        input_text = b"A message for encryption"

        try:
            encrypted_text = rsa_enc_public(input_text, self.key_pair)
        except Exception as exc:
            assert False, f"rsa_enc_public raised an exception {exc}"
        assert encrypted_text is not None

    def test_rsa_dec_private(self):
        input_text = b"A message for encryption"
        encrypted_text = self.generate_encrypted_text(input_text)

        try:
            decrypted_text = rsa_dec_private(encrypted_text, self.key_pair)
        except Exception as exc:
            assert False, f"rsa_dec_private raised an exception {exc}"
        assert decrypted_text == input_text

    def generate_encrypted_text(self, input_text: bytes):
        try:
            encrypted_text = rsa_enc_public(input_text, self.key_pair)
        except Exception as exc:
            assert False, f"rsa_enc_public raised an exception {exc}"

        return encrypted_text
