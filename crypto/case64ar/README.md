# Case64AR
## Cryptography - Easy
| author | prereq chals | first blood | solves | final points |
| --- | --- | --- | --- | --- |
| k3v1n | none | **MikeCAT** from **Team MikeCAT** | 26 | 190 |

### prompt
Someone script kiddie just invented a new encryption scheme. It is described as a blend of modern and ancient cryptographic techniques. Can you prove that the encryption scheme is insecure by decoding the ciphertext below?

**Ciphertext**: OoDVP4LtFm7lKnHk+JDrJo2jNZDROl/1HH77H5Xv

### original specification
Simple encryption on flag with format sdctf{content...}. First apply base64, then apply a Caesar shift on the base64 alphabet. Easily crack-able by brute force once you know how this cipher works

**flag**: `sdctf{OBscUr1ty_a1nt_s3CURITy}`
### writeups
- https://hackmd.io/@ptr-yudai/BJ3BCl8dd#Case64AR
- https://qiita.com/mikecat_mixc/items/5a0c45751b15c8a8513b#case64ar
