import hashlib

URL = b'acmurl.com/covid-challenge'
BLOCK_LENGTH = 32

PASSWORD_OBF_KEY = 13

assert len(URL) < BLOCK_LENGTH

url_c = URL.ljust(BLOCK_LENGTH, b'\0')

def xor(a: bytes, b: bytes):
    assert len(a) == len(b)
    return bytes((ac ^ bc for ac, bc in zip(a, b)))

password = b'd3bugg3rs_ar3_s0_dumb'

enc = xor(url_c, hashlib.sha256(password).digest())

password_enc = bytes((c * PASSWORD_OBF_KEY) & 0xff for c in password)

print('#define FAKE_PASSWORD_LENGTH ({})'.format(len(password)))
print('#define PASSWORD_OBF_KEY ({})'.format(PASSWORD_OBF_KEY))
print('const unsigned char password_enc[] = {' + ','.join(map(hex, password_enc)) + '};')
print('const unsigned char rickroll_url_enc[] = {' + ','.join(map(hex, enc)) + '};')
