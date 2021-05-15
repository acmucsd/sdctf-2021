import hashlib

# sdctf{D1D_1_gET_SIGILL?_U_cant_TELL_bc_tH3RE_4RE_n0_SyMPt0m5!!}
FLAG = b'sdctf{D1D_1_gET_SIGILL?_U_cant_TELL_bc_tH3RE_4RE_n0_SyMPt0m5!!}\0'

password = b'12233123312331231223312331233123312312233123312331233123122331233123312331231223312331233123312312233123312331233123122331233123312312233123312331233123122331233123312331231223312331'

assert len(FLAG) == 64

def xor(a: bytes, b: bytes):
    assert len(a) == len(b)
    return bytes((ac ^ bc for ac, bc in zip(a, b)))



enc = xor(FLAG[0:32], hashlib.sha256(password + b'A').digest()) +\
    xor(FLAG[32:64], hashlib.sha256(password + b'B').digest())

print('const unsigned char flag_enc[] = {' + ','.join(map(hex, enc)) + '};')