from Homework_4_Solution import aes_input_av_test, aes_key_av_test


class TestHomework4:
    def test_input(self):
        plain_text = b"isthis16bytes?"
        key = b"veryverylongkey!"
        bit_list = [5, 29, 38]
        res_bit_list = self.input_test(plain_text, key, bit_list)
        assert res_bit_list == [71, 69, 53]

        plain_text = b"isthissmall"
        key = b"veryverylongkey!"
        bit_list = [5, 29, 38]
        res_bit_list = self.input_test(plain_text, key, bit_list)
        assert res_bit_list == [72, 56, 67]

        plain_text = b"isthissmall"
        key = b"veryverylongkey!"
        bit_list = [5, 8, 38]
        res_bit_list = self.input_test(plain_text, key, bit_list)
        assert res_bit_list == [72, 63, 67]

    def test_key(self):
        plain_text = b"isthis16bytes?"
        key = b"veryverylongkey!"
        bit_list = [5, 29, 38]
        res_bit_list = self.key_test(plain_text, key, bit_list)
        assert res_bit_list == [57, 64, 67]

    @classmethod
    def input_test(cls, plain_text, key, bit_list):
        try:
            return aes_input_av_test(plain_text, key, bit_list)
        except Exception as exc:
            assert False, f"aes_input_av_test failed with error {exc}"

    @classmethod
    def key_test(cls, plain_text, key, bit_list):
        try:
            return aes_key_av_test(plain_text, key, bit_list)
        except Exception as exc:
            assert False, f"aes_key_av_test failed with error {exc}"
