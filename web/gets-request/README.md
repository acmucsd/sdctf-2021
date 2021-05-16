# GETS Request
## Web Exploitation - Easy
| author | prereq chals | first blood | solves | final points |
| --- | --- | --- | --- | --- |
| KNOXDEV | none | **eris** from **Team IRS** | 23 | 234 |

### prompt
Express.JS is an easy-to-use web framework, but Javascript/Typescript is too slow. C is a fast, low level language, but I was tired of debugging memory issues. Can I get the best out of both worlds by combining them? https://gets.sdc.tf

### original specification
An Express.JS application that parses query strings incorrectly by relying on query.length <= BUFFER_SIZE security check where query is a query object and passes query.toString() to a backend C program using the vulnerable gets to get a string into a buffer of size BUFFER_SIZE. Since the default query string parser parses fancy stuff like objects or arrays. You can workaround the buffer size check by passing an array of size 1 in a request (http://example.com/?q[]=evilpayloadAAAAAAAAA%EF%BE%AD%DE), whose toString gives the string inside the array but length is 1 (length of array not string). This allows the participants to perform a buffer overflow attack on the C program and spawn a reverse shell, which will help them get the flag.

**flag**: `sdctf{B3$T_0f-b0TH_w0rLds}`
### writeups
- https://hackmd.io/@ptr-yudai/BJ3BCl8dd#GETS-Request
- https://github.com/thewhitecircle/ctf_writeups/blob/main/sdctf_2021/web.md#gets-request
- https://hackmd.io/@jokr/sdctf-2021-gets-request
- https://github.com/3vilbuff3r/ctf-writeups/blob/master/sdctf-2021/web/gets-request.md
