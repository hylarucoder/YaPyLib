"""
1. md5
2. base64
3. sha1
4. sha256
"""
import base64
import hashlib


def md5(s, encoding='utf-8'):
    m = hashlib.md5()
    m.update(s.encode(encoding))
    return m.hexdigest()


def base64_encode(s):
    if isinstance(s, str):
        s = s.encode()
    return base64.b64encode(s).decode('ascii')

