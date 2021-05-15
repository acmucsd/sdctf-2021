yes = b'yeet'

pid_string_start = b'ONCE'

LENGTH = 4

def encrypt(plain):
    return bytes([((plain[i] ^ (pid_string_start[i] - i * i)) + i * i * i) % 256 for i in range(LENGTH)])

def decrypt(cipher):
    return bytes([((cipher[i] - i * i * i) ^ (pid_string_start[i] - i * i)) % 256 for i in range(LENGTH)])

print(encrypt(yes))
# assert decrypt(encrypt(yes)) == yes
