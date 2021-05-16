# No flag for you
## Misc - Medium
| author | prereq chals | first blood | solves | final points |
| --- | --- | --- | --- | --- |
| k3v1n | none | **LCF** from **Team LCF** | 36 | 450 |

### prompt
Welcome to the most restrictive shell ever, with only 2 semi-functional non-shell commands.

Connect via:
`nc noflag.sdc.tf 1337`

**attachments**: `Do not provide anything!`
### original specification
Make a script that runs system() with a string rbash -c ' concatenated with user input and appended with '. Before doing so please restrict PATH. the path should only contain custom self written programs that runs confusing things (Ex. cat binary printing No flag for you for every file and ls that fools the user into thinking that a certain directory is empty when it is not)

The participant must figure out that they are running in a restricted shell and that the vulnerability is shell injection (due to concatenation). The file is not provided to them

**flag**: `sdctf{1t'5_7h3_sh3ll_1n_4_shEll}`
### writeups
- https://hackmd.io/@ptr-yudai/BJ3BCl8dd#No-flag-for-you
- https://github.com/thewhitecircle/ctf_writeups/blob/main/sdctf_2021/misc.md#no-flag-for-you
- https://szymanski.ninja/en/ctfwriteups/2021/sdctf/no-flag-for-you/
- https://github.com/anandrajaram21/CTFs/blob/main/SanDiegoCTF/misc/no-flag-for-you/writeup.md
- https://github.com/3vilbuff3r/ctf-writeups/blob/master/sdctf-2021/misc/no-flag-for-you.md
