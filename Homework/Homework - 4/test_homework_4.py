from Homework_4_Solution import aes_input_av_test, aes_key_av_test


class TestHomework4:
    def test_input(self):
        plain_text = b"isthis16bytes?"
        key = b"veryverylongkey!"
        bit_list = [5, 29, 38]
        res_bit_list = aes_input_av_test(plain_text, key, bit_list)
        assert res_bit_list == [71, 69, 53]

    def test_key(self):
        plain_text = b"isthis16bytes?"
        key = b"veryverylongkey!"
        bit_list = [5, 29, 38]
        res_bit_list = aes_key_av_test(plain_text, key, bit_list)
        assert res_bit_list == [57, 64, 67]
