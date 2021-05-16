# Git Good
## Web Exploitation - Medium
| author | prereq chals | first blood | solves | final points |
| --- | --- | --- | --- | --- |
| KNOXDEV | none | **eris** from **Team IRS** | 57 | 349 |

### prompt
We've been issued a challenge by the primary competing cyber organization on campus, the Cybersecurity Group at UCSD. You have been granted permission to try and hack into their admin portal to steal their flag. They've been hardening their website for some time now, and they said they think its "unhackable". Show them how wrong they are!

https://cgau.sdc.tf

### original specification
Basically an exposed git repo on a webserver that allows the exfiltration of the program source code and database. Rolling back to an old commit allows the user to see an older version of the database containing weaker, crackable hashes.

**flag**: `sdctf{1298754_Y0U_G07_g00D!}`
### writeups
- https://0x0elliot.medium.com/git-good-a-web-ctf-dealing-with-broken-git-commits-f879163557f9
- https://github.com/anandrajaram21/CTFs/blob/main/SanDiegoCTF/web/git-good/writeup.md
- https://github.com/thewhitecircle/ctf_writeups/blob/main/sdctf_2021/web.md#git-good
- https://hackmd.io/@ptr-yudai/BJ3BCl8dd#Git-Good
