import sys, os, random

print("Python", sys.version)

if sys.version_info >= (3, 3):
    # Python 3.3.0: PEP 420, namespace package support
    from src import base64NoUpperCase
else:
    sys.path.insert(0, os.path.abspath("src"))
    import base64NoUpperCase

if hasattr(random, "randbytes"):
    randbytes = random.randbytes  # Added in version 3.9.
else:
    from os import urandom as randbytes


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
