# Apollo 1337
## Web Exploitation - Easy
| author | prereq chals | first blood | solves | final points |
| --- | --- | --- | --- | --- |
| KNOXDEV | none | **ziot** from **Team HackingForSoju** | 55 | 103 |

### prompt
Hey there intern! We have a rocket launch scheduled for noon today and the launch interface is down. You'll need to directly use the API to launch the rocket. No, we don't have any documentation. And quickly, our shareholders are watching!

https://space.sdc.tf

### original specification
A space-themed website with a REST API with no documentation on how to use it, but the API will give very verbose errors on what is missing in your query, allowing you to reverse engineer the API and submit the correct query with the missing parameters. The punchline is that it will ask for a token as the final missing piece, which can only be found in minified JS source code.

**flag**: `sdctf{0ne_sM@lL_sT3p_f0R_h@ck3r$}`
### writeups
- https://securitytaters.info/solving-apollo-1337-from-san-diego-ctf-2021.html
- https://github.com/3vilbuff3r/ctf-writeups/blob/master/sdctf-2021/web/appollo-1337.md
- https://github.com/anandrajaram21/CTFs/blob/main/SanDiegoCTF/web/apollo-1337/writeup.md
- https://github.com/thewhitecircle/ctf_writeups/blob/main/sdctf_2021/web.md#apollo-1337
- https://hackmd.io/@ptr-yudai/BJ3BCl8dd#Apollo-1337
