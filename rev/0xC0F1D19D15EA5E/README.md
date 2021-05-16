# 0xC0F1D19D15EA5E
## Reversing - Hard
| author | prereq chals | first blood | solves | final points |
| --- | --- | --- | --- | --- |
| k3v1n | none | **keymoon** from **Team zer0pts** | 6 | 973 |

### prompt
This binary has been vaccinated for 0xC0F1D19, the reverse engineer's virus. Can you demonstrate the ineffectiveness of this vaccine?

**attachments**: `0xC0F1D`
### original specification
Make some anti-RE binary. Examples of obfuscation that can be used:
1. Anti-debugging ptrace trick + Anti VM/strace (like CSAW's goaway.c)
2. Debugger/emulator/container (Ex. Docker) identification via timing and parent process identification. Exit itself if not ran as root to make debugging even harder.
3. Executing code on stack, runtime decryption of code (Maybe use GenuineIntel from CPUID as the Vigenere-XOR key, utilizing hardware details)
4. Integrity check (combined with anti-debugging) to guard against patching
5. Enforced memory address space layout randomization through mmaping pages preferably at address chosen by /dev/urandom

Some creative ideas:
1. When it detects a debugger, running in a virtual machine, emulator, or hooked libc, make it say Virtual Machines, Debuggers, Emulators, etc. must stay 6 feet apart from this program per social distancing guidelines.
2. Requires you to set environment variable MASK_ON=true or it will error out and say The computer must be wearing a mask to run this program. This can be enforced by encrypting most of the program with the key true which is sourced from the environment variable if it exists.

Update 2:37pm 5/9:
Minimum point changed from 900 to 700 as 6 people solved this.

**flag**: `sdctf{D1D_1_gET_SIGILL?_U_cant_TELL_bc_tH3RE_4RE_n0_SyMPt0m5!!}`
### writeups
- https://hackmd.io/@ptr-yudai/BJ3BCl8dd#0xC0F1D19D15EA5E
