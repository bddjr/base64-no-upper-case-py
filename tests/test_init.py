import random
import base64NoUpperCase


def test_init():
    print()

    def t(input: bytearray | bytes | str):
        print(input)
        enc = base64NoUpperCase.encode(input)
        print(enc)
        if isinstance(input,str):
            dec = base64NoUpperCase.decodeToStr(enc)
        else:
            dec = base64NoUpperCase.decode(enc)
        print(dec)
        assert input == dec
        print()

    t("hello world")
    t("Hello world!")
    t("1234567")
    t("12345678")
    t("123456789")
    t(random.randbytes(7))
    t(random.randbytes(8))
    t(random.randbytes(9))
