# HAXLAB — Flag Leak
## Pwn - Medium
| author | prereq chals | first blood | solves | final points |
| --- | --- | --- | --- | --- |
| k3v1n | none | **PinkNoize** from **Team HashSlingingHackers** | 22 | 378 |

### prompt
Welcome to HAXLAB, the world's most secure MaaS® (math-as-a-service) with advanced functionality.

For this part of the challenge, you need to submit `flag1.txt`.

Connect with `nc haxlab.sdc.tf 1337`.

**attachments**: `jail.py`
### original specification
Current name is a variation of the proprietary software MATLAB from MathWorks. Original name: snake_dungeon. Make a Python 3 Jail/Sandbox designed to make it difficult to run arbitrary code (breaking out of the jail) with untrusted input, but still allows users to run calculations (maybe numpy?).

It works by installing an audit hook, the participant must monkey-patch the set() function to disable the audit hook.

Update 9:47pm 5/8/2021:
Difficulty increased from Easy to Medium. Max/Initial Point value increased from 200 to 400

**flag**: `sdctf{get@ttr_r3ads_3v3ryth1ng}`
### writeups
- https://hackmd.io/@ptr-yudai/BJ3BCl8dd#HAXLAB-%E2%80%94-Flag-Leak
- https://qiita.com/mikecat_mixc/items/5a0c45751b15c8a8513b#haxlab--flag-leak
- https://szymanski.ninja/en/ctfwriteups/2021/sdctf/haxlab-flag-leak/
- https://github.com/3vilbuff3r/ctf-writeups/blob/master/sdctf-2021/pwn/haxlab-flag-leak.md

# HAXLAB — Endgame Pwn
## Pwn - Hard
| author | prereq chals | first blood | solves | final points |
| --- | --- | --- | --- | --- |
| k3v1n | HAXLAB - Flag Leak | **PinkNoize** from **Team HashSlingingHackers** | 6 | 648 |

### prompt
Same Python script and same host and port as "HAXLAB — Flag Leak", but you need to demonstrate arbitrary code execution by submitting flag2.txt.

**attachments**: `jail.py`
### original specification
Same host and port with HAXLAB - Flag Leak

Update 9:50pm 5/8/2021:

Max point value increased from 400 to 650. Difficulty becomes Hard

**flag**: `sdctf{4ud1t_hO0ks_aR3_N0T_SaNDB0x35}`
### writeups
- https://hackmd.io/@ptr-yudai/BJ3BCl8dd#HAXLAB-%E2%80%94-Endgame-Pwn
- https://qiita.com/mikecat_mixc/items/5a0c45751b15c8a8513b#haxlab--endgame-pwn
