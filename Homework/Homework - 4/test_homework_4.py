from Homework_4_Solution import aes_input_av_test, aes_key_av_test


class TestHomework4:
    def test_final(self):
        res = aes_input_av_test(b"isthis16bytes?", b"veryverylongkey!", [5, 29, 38])
        assert res == [71, 69, 53]

        res = aes_key_av_test(b"isthis16bytes?", b"veryverylongkey!", [5, 29, 38])
        assert res == [57, 64, 67]

        res = aes_input_av_test(b"ip8bytes", b"thisoneslongbyte", [35, 72, 110])
        assert res == [71, 65, 67]

        res = aes_key_av_test(b"ip8bytes", b"thisoneslongbyte", [35, 72, 110])
        assert res == [64, 68, 59]

        res = aes_input_av_test(b"passthistestcase", b"thisoneslongbyte", [0, 63, 127])
        assert res == [57, 66, 70]

        res = aes_key_av_test(b"passthistestcase", b"thisoneslongbyte", [0, 63, 127])
        assert res == [61, 66, 70]
