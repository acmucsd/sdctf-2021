# Major Change Application
## Reversing - Hard
| author | prereq chals | first blood | solves | final points |
| --- | --- | --- | --- | --- |
| k3v1n | none | **ptr-yudai** from **Team zer0pts** | 6 | 699 |

### prompt
The University of Coral Sea at Diamondville (UCSD) has recently opened up an application for students to change their majors into its world-renowned Computer Science major. Unfortunately, due to the volume of the incoming application (~ 2^64), it decided to admit students based on a lottery. Only 10 people will be admitted, and they will be given the secret flag which they must present to professors before enrolling in the upper division courses.

Fortunately, you hacked into their computer systems and retrieved a binary executable responsible for performing the lottery (you don't dare tampering with its systems and modifying any data since any evidence of that would surely get you expelled), and it seems that its algorithm is flawed...

Connect via: `nc major.sdc.tf 1337`

**attachments**: `chal.out`
### original specification
- The binary seeds its own [LCG](https://en.wikipedia.org/wiki/Linear_congruential_generator) random number generator using the current system time in seconds since epoch (Unix time: `time(2)`), the name of the applicant (hashed by summing up all the character ASCII values or any naive way), the student PID (validated using a crackable algorithm similar to product keys), and the email address (validated)
- PID must start with a letter (like A)
- Validation performed on PID - name correspondence
- Eventually it checks that the result of the final LCG generation must be the largest 10 `uint64_t` numbers.

**flag**: `sdctf{I_f1nally_h@v3_@ccess_t0_Upp3r_d1v_c0ur535}`
### writeups
- https://hackmd.io/@ptr-yudai/BJ3BCl8dd#Major-Change-Application