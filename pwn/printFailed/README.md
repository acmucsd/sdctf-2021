# printFAILED
## Pwn - Medium
| author | prereq chals | first blood | solves | final points |
| --- | --- | --- | --- | --- |
| green beans | none | **ptr-yudai** from **Team zer0pts** | 52 | 206 |

### prompt
I'm new to C. I just learned printf and everything just worked™. But my friend Greg, who works at a security company, tells me that some strings crashed the program but refused to tell me specifically which ones. (He wanted to publish those in DEF CON). Can you find the magic string before he carry out his evil plan?

Connect via: `nc printf.sdc.tf 1337`

**attachments**: `print-failed: The vulnerable binary`
### original specification
Make a binary that executes printf on arbitrary user input.

**flag**: `sdctf{D0nt_b3_4_f41lur3_1ik3_tH1S_C0d3}`
### writeups
- https://hackmd.io/@ptr-yudai/BJ3BCl8dd#printFAILED
- https://github.com/thewhitecircle/ctf_writeups/blob/main/sdctf_2021/pwn.md#printfailed
- https://qiita.com/mikecat_mixc/items/5a0c45751b15c8a8513b#printfailed
- https://szymanski.ninja/en/ctfwriteups/2021/sdctf/printfailed/
