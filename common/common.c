#include "common.h"

void die(void) {
    exit(EXIT_FAILURE);
}

// read_input reads a line of input and removes line terminators, similar to Python 3's input
void read_input(char *buffer, int size) {
    fflush(stdout); // first flush all outputs before getting input
    if (fgets(buffer, size, stdin) == NULL) {
        // error handling
        if (feof(stdin)) {
            MSG_DEBUG("EOF!");
            exit(EXIT_SUCCESS);
        }
        // must have failed
        // #ifdef DEBUG
        // perror("fgets: Read from stdin failed");
        // #endif
        PERROR_FATAL("read_input: Read from stdin failed");
    }
    // Replace newline, if any, with the null byte
    for (int i = 0; i < size; i++) {
        if (buffer[i] == '\n') {
            buffer[i] = '\0';
            break;
        } else if (buffer[i] == '\0') {
            break;
        }
    }
}

char ck_getchar(void) {
    int result = getchar();
    if (result == EOF) {
        MSG_DEBUG("EOF!");
        die();
    }
    return (char) result;
}

// if the strings are equal, return 1, else 0
int timing_safe_equal(char *s1, char *s2, size_t length) {
    volatile int fail = 0;
    for (size_t i = 0; i < length; i++) {
        fail |= s1[i] ^ s2[i];
    }
    return !fail;
}
