"""
Base64, but no UPPER CASE.

It is useful in case-insensitive scenarios, such as Scratch.
"""

import binascii, sys

# from typing import TYPE_CHECKING  # Added in version 3.5.2.
TYPE_CHECKING = False

if TYPE_CHECKING:
    if sys.version_info >= (3, 12):
        from _collections_abc import Buffer  # Added in version 3.12.
    else:
        from typing import Any as Buffer


__all__ = ["CHAR_MAP", "b64encode", "b64decode"]

CHAR_MAP = "!#$%&()*,-.:;<>?@[]^_`{|}~abcdefghijklmnopqrstuvwxyz0123456789+/"

_upperCharMap = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_noUpperCharMap = b"!#$%&()*,-.:;<>?@[]^_`{|}~"

_encode_translation = bytes.maketrans(_upperCharMap, _noUpperCharMap)
_decode_translation = bytes.maketrans(_noUpperCharMap, _upperCharMap)


def _bytes_from_encode_data(s: "str | Buffer"):
    if isinstance(s, str):
        try:
            return s.encode()
        except UnicodeEncodeError:
            raise ValueError("string argument should contain only ASCII characters")
    return s


def _bytes_from_decode_data(s: "str | Buffer"):
    if isinstance(s, str):
        try:
            return s.encode("ascii")
        except UnicodeEncodeError:
            raise ValueError("string argument should contain only ASCII characters")
    if isinstance(s, (bytes, bytearray)):
        return s
    try:
        return memoryview(s).tobytes()
    except TypeError:
        raise TypeError(
            "argument should be a bytes-like object or ASCII "
            "string, not %r" % s.__class__.__name__
        ) from None


def b64encode(s: "str | Buffer") -> bytes:
    return binascii.b2a_base64(_bytes_from_encode_data(s), newline=False).translate(
        _encode_translation
    )


if sys.version_info >= (3, 11):

    def b64decode(s: "str | Buffer", validate: bool = False) -> bytes:
        s = _bytes_from_decode_data(s).translate(_decode_translation)
        if len(s) % 4 != 0:
            s += b"=" * (4 - (len(s) % 4))
        return binascii.a2b_base64(s, strict_mode=validate)

else:

    def b64decode(s: "str | Buffer") -> bytes:
        s = _bytes_from_decode_data(s).translate(_decode_translation)
        if len(s) % 4 != 0:
            s += b"=" * (4 - (len(s) % 4))
        return binascii.a2b_base64(s)
