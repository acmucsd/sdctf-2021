# $ safe-unix-playground # rm -rf /
## Cryptography - Medium
| author | prereq chals | first blood | solves | final points |
| --- | --- | --- | --- | --- |
| RJ | none | **vishiswoz** from **Team ARESx** | 15 | 443 |

### prompt
Welcome to my awesome Unix command playground offered over a TCP port! With the free plan, you can run only example commands we provide. To run any other command, you will need to contact us for a premium partnership plan (Update 04/01/2020: premium plan cancelled due to COVID-19).

Connect via:
`nc unix.sdc.tf 1337`

### original specification
Make a program that runs shell commands given by the user, but supposedly only a whitelist of "Trusted" commands can execute. For example, this can be
ls
cat fake-flag.txt
echo hello world
However, the whitelist is implementing by checking whether the hash of the command is equal to a hash whitelist, but the hash function is prone to collisions with attacker-chosen command (Ex. MD5)

The participant need to be able to find a command like cat real-flag.txt #any comment is fine here that has the same hash as one of the "trusted" commands.

**flag**: `sdctf{MD5_iS_DeAd!L0ng_l1v3_MD5!}`
### writeups
- https://hackmd.io/@ptr-yudai/BJ3BCl8dd#-safe-unix-playground--rm--rf-
- https://github.com/3vilbuff3r/ctf-writeups/blob/master/sdctf-2021/crypto/safe-unix-playground-rm-rf.md
