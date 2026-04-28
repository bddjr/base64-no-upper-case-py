# Windows: py -m pytest
# Other: python3 -m pytest

import random, os
import base64NoUpperCase

if hasattr(random, "randbytes"):
    randbytes = random.randbytes
else:
    randbytes = os.urandom


def test_init():
    print()

    def t(s: "str | bytes"):
        print(s)
        enc = base64NoUpperCase.b64encode(s)
        print(enc)
        dec = base64NoUpperCase.b64decode(enc)
        if isinstance(s, str):
            dec = dec.decode()
        print(dec)
        assert s == dec
        print()

    t("hello world")
    t("Hello world!")
    t("1234567")
    t("12345678")
    t("123456789")
    t(randbytes(7))
    t(randbytes(8))
    t(randbytes(9))
    t("你好👋")

    print(base64NoUpperCase.b64decode("x+"))
    print(base64NoUpperCase.b64decode("x++"))
