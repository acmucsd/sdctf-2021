#ifndef __COMMON_H_INCLUDED
#define __COMMON_H_INCLUDED

#include <stdio.h>
#include <stdlib.h>

// MSG_DEBUG is for debug infos (Ex. participant errors, like nonsatisfied constraints in reversing challenges),
// should not be shown in either deploy or participant version (only in debug)
// PERROR_FATAL is for **fatal** errors that must terminate the program. It is usually due to misconfigurations
// Message is shown in either debug _or_ deploy mode.
// Ex. File not found, read/write over network failed

#ifdef DEBUG
    #define MSG_DEBUG(msg) {fputs("[+] DEBUG: " msg, stderr); fputs("\n", stderr);}
    #define PERROR_FATAL(msg) {perror(msg); exit(EXIT_FAILURE);}
#else
    #define MSG_DEBUG(msg) {}
    // DEPLOY define sample use case:
    // server side binary that accepts connections from participants over network ports (usually requires the client to connect via `nc <host> <port>`),
    // the binary must **not** be given to the participant (as it eases reversing) but the participant may still observe its behavior
    #ifdef DEPLOY
        #define PERROR_FATAL(msg) {perror(msg); puts("Something went wrong. Please contact an admin and give them the following message: " msg); exit(EXIT_FAILURE);}
    #else
        #define PERROR_FATAL(msg) {puts("Something went wrong."); exit(EXIT_FAILURE);}
    #endif
#endif

void read_input(char *buffer, int size);
void die(void);
char ck_getchar(void);
int timing_safe_equal(char *s1, char *s2, size_t length);

// useful macro to frustrate reverse engineers without sacrificing code readability and debuggability for challenge devs
#ifdef DEBUG
    // make it easier to debug for admins
    #define FORCE_INLINE
#else
    #define FORCE_INLINE inline __attribute__((always_inline))
#endif

#endif // #ifndef __COMMON_H_INCLUDED
