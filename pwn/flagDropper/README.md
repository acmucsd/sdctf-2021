# Flag dROPper
## Pwn - Easy
| author | prereq chals | first blood | solves | final points |
| --- | --- | --- | --- | --- |
| green beans | none | **zzz** from **Team Kalmarunionen** | 42 | 216 |

### prompt
I heard that gadgets are very easy to find in C programs, so I coded my program in assembly to protect my program from hackers.

Connect via: `nc dropper.sdc.tf 1337`

**attachments**: `flag-dropper: The vulnerable binary`
### original specification
A simple ROP exploit, but unlike the boring ROP exploit usable in any C program with minimal modification (That is, finding pop rdi; ret and overwrite the return address so that it points to that gadget) The code is written from nasm with no dependency on libc. Yet there is a "win function" that spawns a shell in the binary when it detects that its argument is a string like sdwin.

**flag**: `sdctf{n1C3_C4tcH_bUd}`
### writeups
- https://blackbeard666.github.io/pwn_exhibit/content/2021_CTF/sandiegoCTF/flagdropper.html
- https://github.com/3vilbuff3r/ctf-writeups/blob/master/sdctf-2021/pwn/flag-dropper.md
- https://qiita.com/mikecat_mixc/items/5a0c45751b15c8a8513b#flag-dropper
- https://github.com/thewhitecircle/ctf_writeups/blob/main/sdctf_2021/pwn.md#flag-dropper
- https://hackmd.io/@ptr-yudai/BJ3BCl8dd#Flag-dROPper
