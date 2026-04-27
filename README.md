Base64, but no UPPER CASE.

It is useful in case-insensitive scenarios, such as Scratch.

```
!#$%&()*,-.:;<>?@[]^_`{|}~abcdefghijklmnopqrstuvwxyz0123456789+/
```

For Scratch:  
<https://scratch.mit.edu/projects/1263900629/>  

For JavaScript:  
<https://www.npmjs.com/package/base64-no-upper-case>  

## Setup

```
pip3 install base64-no-upper-case
```

```py
import base64NoUpperCase

# Encode bytes to bytes
enc = base64NoUpperCase.b64encode(random.randbytes(7))
print(enc)

# Decode bytes to bytes
dec = base64NoUpperCase.b64decode(b'q-784344h@==')
print(dec)

# Encode str to str
enc = base64NoUpperCase.b64encode("Hello world!").decode()
print(enc)

# Decode str to str
dec = base64NoUpperCase.b64decode("])`sb)8gd29yb)@h").decode()
print(dec)
```
