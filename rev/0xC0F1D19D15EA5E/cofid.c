#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <fcntl.h>
#include <signal.h>
#include <ucontext.h>
#include <unistd.h>
#include <ctype.h>

// #include <sys/ptrace.h>

// OpenSSL
#include <openssl/md5.h>
#include <openssl/sha.h>
#include <openssl/crypto.h>

#include "common.h"

void debugger_warning(void);

// Workaround for VSCode intellisense bug: https://github.com/microsoft/vscode-cpptools/issues/4503
#if __INTELLISENSE__
#pragma diag_suppress 1094
#endif

#define UD2_LENGTH 3
#define UD2_FUNC_OFFSET 2
// funcnum expanded as a string
#define _UD2(funcnum) {__asm__ volatile ( "ud2\n\t"  ".byte " #funcnum );}
// funcnum can be a macro here
#define UD2(funcnum) _UD2(funcnum)
// #define UD2(funcnum)

// UD2 function constants
#define FUNC_DO_NOTHING 0x00
#define FUNC_SET_REAL_ENTRY 0x01
#define FUNC_POUR 0x02
#define FUNC_DEBUG_WARNING 0x03

#define PASSWORD_PROMPT "Enter password: "

// 3 Jug problem: https://en.wikipedia.org/wiki/Water_pouring_puzzle
#define N_JUGS 3

// int capacities[] = {92, 73, 19};
// // Modified in ud2_handler so must be volatile
// volatile int current_amount[] = {92, 0, 0};
// int correct_final_amount[] = {46, 46, 0};

#define CAPACITY_1 92
#define CAPACITY_2 73
#define CAPACITY_3 19

#define STARTING_AMOUNT_1 CAPACITY_1
#define FINAL_AMOUNT_1 46
#define FINAL_AMOUNT_2 46
#define FINAL_AMOUNT_3 0

// Correct values will be assigned based on decrypting with a hash in main()
int capacities[] = {0, 0, 0};
// Modified in ud2_handler so must be volatile
volatile int current_amount[] = {0, 0, 0};
int correct_final_amount[] = {0, 0, 0};

// minimum steps required to solve the puzzle
#define STEP_COUNT 91

/* debug */
// int capacities[] = {8, 5, 3};
// // Modified in ud2_handler so must be volatile
// volatile int current_amount[] = {8, 0, 0};
// int correct_final_amount[] = {4, 4, 0};
// // minimum steps required to solve the puzzle
// #define STEP_COUNT 7

#define PASSWORD_LENGTH (STEP_COUNT*2)

volatile int pour_from;
volatile int pour_to;

// Encrypted flag buffer
// Will be modified in place when decrypting
unsigned char flag_enc[] = {0x5a,0x7,0x24,0x19,0xc1,0xc,0xe1,0x4c,0x63,0x3a,0x9b,0x3c,0xf8,0x1f,
                            0x50,0xeb,0x93,0x54,0xa6,0xef,0x47,0x34,0x66,0x49,0xe0,0x98,0xc2,0x28,
                            0x54,0x48,0xa2,0xfa,0x44,0xe5,0x74,0x89,0xf1,0x78,0x72,0x29,0x78,0xcf,
                            0xd9,0x3d,0xeb,0xe,0x4,0xe5,0x41,0x46,0xf2,0x20,0x5f,0x16,0xa8,0x17,
                            0xea,0xb1,0xaf,0xbb,0x98,0x3a,0x9f,0xa5};

void xor_flag(int start, int end, unsigned char *cipher_buf) {
    for (int i = start; i < end; i++) {
        flag_enc[i] ^= cipher_buf[i - start];
    }
}

FORCE_INLINE void decrypt_and_print_flag(char *input_password) {
    // modifies input_password's terminating null byte to simplify code
    input_password[PASSWORD_LENGTH] = 'A';
    xor_flag(0, 32, SHA256((unsigned char *) input_password, PASSWORD_LENGTH + 1, NULL));
    input_password[PASSWORD_LENGTH] = 'B';
    xor_flag(32, 64, SHA256((unsigned char *) input_password, PASSWORD_LENGTH + 1, NULL));
    puts((char *) flag_enc);
}

void wrong_pw(void) {
    puts("Incorrect password. Get out!");
    exit(EXIT_FAILURE);
}

// call this when password is the correct one to the fake entry
void rickroll(char *url) {
    puts("WOOOOOW! You are so amazing and cracked this uncrackable binary!");
    printf("---->  Here's the link to the flag: https://%s  <----\n", url);
    UD2(FUNC_DEBUG_WARNING);
    sleep(5);
    debugger_warning();
}

#define FAKE_PASSWORD_LENGTH (21)
#define PASSWORD_OBF_KEY (13)
const unsigned char password_enc[] = {0x14,0x97,0xfa,0xf1,0x3b,0x3b,0x97,0xca,0xd7,0xd3,0xed,0xca,
                             0x97,0xd3,0xd7,0x70,0xd3,0x14,0xf1,0x89,0xfa};
// Encrypted rickroll URL buffer
// Will be modified in place when decrypting
unsigned char rickroll_url_enc[] = {0x74,0x42,0x51,0x59,0x87,0x53,0xd9,0xc0,0x92,0xe8,0x5e,0x6a,0xa4,
                                    0xdc,0x59,0x6b,0x5e,0xf3,0x2b,0x29,0x73,0xeb,0x15,0x63,0x38,0x56,
                                    0xe8,0x50,0xa4,0x81,0xd0,0xda};

void fake_entry(void) {
    printf(PASSWORD_PROMPT);
    char password[FAKE_PASSWORD_LENGTH+2];
    read_input(password, FAKE_PASSWORD_LENGTH+2);
    size_t pwlen = strlen(password);
    if (pwlen != FAKE_PASSWORD_LENGTH) {
        MSG_DEBUG("Wrong fake password length!");
        wrong_pw();
    }
    for (int i = 0; i < FAKE_PASSWORD_LENGTH; i++) {
        if ((unsigned char) ((unsigned char) password[i] * PASSWORD_OBF_KEY) != password_enc[i]) {
            MSG_DEBUG("Fake password content incorrect!");
            wrong_pw();
        }
    }
    unsigned char *cipher_buf = SHA256((unsigned char *) password, FAKE_PASSWORD_LENGTH, NULL);
    for (int i = 0; i < 32; i++) {
        rickroll_url_enc[i] ^= cipher_buf[i];
    }
    rickroll((char *) rickroll_url_enc);
}

void real_entry(void) {
    printf(PASSWORD_PROMPT);
    char input_password[PASSWORD_LENGTH+2]; // account for newline and terminating NUL
    read_input(input_password, PASSWORD_LENGTH+2);
    size_t pwlen = strlen(input_password);
    if (pwlen != PASSWORD_LENGTH) {
        MSG_DEBUG("Wrong password length!");
        wrong_pw();
    }
    for (int i = 0; i < PASSWORD_LENGTH; i++) {
        if (input_password[i] < '1' ||
            input_password[i] > (char)('0' + N_JUGS)) {
            MSG_DEBUG("Invalid characters in password!");
            wrong_pw();
        }
    }
    MSG_DEBUG("Password structure is valid!");

    for (int i = 0; i < STEP_COUNT; i++) {
        pour_from = input_password[i * 2] - '1';
        pour_to = input_password[i * 2 + 1] - '1';
        UD2(FUNC_POUR);
    }

    for (int i = 0; i < N_JUGS; i++) {
        if (current_amount[i] != correct_final_amount[i]) {
            MSG_DEBUG("Final jug amount is incorrect!");
            wrong_pw();
        }
    }
    
    puts("Good job! Here's the flag: ");
    decrypt_and_print_flag(input_password);
}

void (*volatile entry)(void) = fake_entry;

// depends on static parameters pour_from and pour_to
FORCE_INLINE void pour(void) {
    if (pour_to == pour_from) {
        // Do nothing when pouring with the same source and target
        return;
    }
    int emptiness_to = capacities[pour_to] - current_amount[pour_to];
    int pour_amount = current_amount[pour_from];
    if (emptiness_to < current_amount[pour_from]) {
        pour_amount = emptiness_to;
    }
    current_amount[pour_from] -= pour_amount;
    current_amount[pour_to] += pour_amount;
}

void debugger_warning(void) {
    puts("Trolled? Debuggers must stay 6 feet away from this program!\n"
        "Attempts to debug include the use of preloading, or setting LD_* environment variables.");
    exit(EXIT_FAILURE);
}

void debugger_warning_handler(__attribute__ ((unused)) int sig) {
    debugger_warning();
}

FORCE_INLINE void setup_debug_warning(void) {
    int signals[] = {SIGINT, SIGTERM};
    for (int i = 0; i < (int) (sizeof(signals) / sizeof(int)); i++) {
        if (signal(signals[i], debugger_warning_handler) == SIG_ERR) {
            PERROR_FATAL("signal: unable to set handler");
        }
    }
}

void ud2_handler(__attribute__ ((unused)) int sig, __attribute__ ((unused)) siginfo_t *info, void *context) {
    ucontext_t *ucontext = (ucontext_t *) context;
    const unsigned char *pc = (const unsigned char *) (ucontext->uc_mcontext.gregs[REG_RIP]);
    int func_byte = pc[UD2_FUNC_OFFSET];
    switch (func_byte) {
        case FUNC_DO_NOTHING:
            MSG_DEBUG("UD2: Do nothing");
            break;
        
        case FUNC_SET_REAL_ENTRY:
            MSG_DEBUG("UD2: Setting `entry` to point to `real_entry`");
            entry = real_entry;
            break;
        
        case FUNC_POUR:
            MSG_DEBUG("UD2: Pouring...");
            pour();
            break;
        
        case FUNC_DEBUG_WARNING:
            MSG_DEBUG("Setting up debug warning handler");
            setup_debug_warning();
            break;

        default:
            MSG_DEBUG("UD2: Unknown function");
            // printf("[+] UD2: Function number: %#x\n", (unsigned int) func_byte);
            break;
    }
    // skip over ud2
    ucontext->uc_mcontext.gregs[REG_RIP] += UD2_LENGTH;
}

// echo -n true | md5sum
// b326b5062b2f0e69046810717534cb09
#define TRUE_LENGTH 4
const unsigned char MD5_TRUE[] = {0xb3, 0x26, 0xb5, 0x06, 0x2b, 0x2f, 0x0e, 0x69, 0x04, 0x68, 0x10, 0x71, 0x75, 0x34, 0xcb, 0x09};

FORCE_INLINE bool is_mask_on(const char *mask_status) {
    // return !strcmp(mask_status, "true");
    return strlen(mask_status) == TRUE_LENGTH &&
           !CRYPTO_memcmp(
               MD5((const unsigned char *) mask_status, TRUE_LENGTH, NULL),
               MD5_TRUE, sizeof(MD5_TRUE));
}

// Priority of 101 means it runs before kickout_reverse_engineers
__attribute__((constructor (101)))
void setup_ud2_handler(void) {
    struct sigaction act;
    act.sa_sigaction = ud2_handler;
    sigemptyset(&act.sa_mask);
    act.sa_flags = SA_SIGINFO;
    if (sigaction(SIGILL, &act, NULL)) {
        PERROR_FATAL("sigaction");
    }
}

#define STATUS_BUF_SIZE 4096
#define TRACER_PID_STR "TracerPid:"

// Adapted from code by StackOverflow users Sam Liao and Violet Giraffe:
// https://stackoverflow.com/a/24969863
// Modified to remove '::', close /proc/self/status after use, and obfuscate path names
// License: CC BY-SA 4.0 https://creativecommons.org/licenses/by-sa/4.0/
bool isDebuggerAttached() {
    char buf[STATUS_BUF_SIZE];

    const int status_fd = open("//./proc//.//./self////./status", O_RDONLY);
    if (status_fd == -1) return false;

    const ssize_t num_read = read(status_fd, buf, sizeof(buf) - 1);
    if (num_read <= 0) {
        close(status_fd);
        return false;
    }

    buf[num_read] = '\0';
    const char *tracer_pid_ptr = strstr(buf, TRACER_PID_STR);
    if (!tracer_pid_ptr) {
        close(status_fd);
        return false;
    }

    for (const char *characterPtr = tracer_pid_ptr + sizeof(TRACER_PID_STR) - 1;
         characterPtr <= buf + num_read; ++characterPtr) {
        if (isspace(*characterPtr))
            continue;
        else {
            close(status_fd);
            return isdigit(*characterPtr) && *characterPtr != '0';
        }
    }

    close(status_fd);
    return false;
}

// Make it more obscure by including it in the constructor
__attribute__((constructor (102)))
void troll_reverse_engineers(void) {
    #ifndef DEBUG
    if (isDebuggerAttached())
        return;
    // anti analysis instruction sequence
    UD2(FUNC_DO_NOTHING);
    // No syscalls are needed for getenv as it is passed on the stack before the program runs
    // Catchpoints will not catch this
    if (getenv("LD_PRELOAD") || getenv("LD_LIBRARY_PATH"))
        return;
    if (open("/etc/ld.so.preload", O_RDONLY) != -1)
        return;

    // If any branch returns early, then the function will be left in the fake state
    UD2(FUNC_SET_REAL_ENTRY);
    #endif
}

int main(void) {
    const char *mask_on = getenv("MASK_ON");
    // if (mask_on == NULL) {
    //     puts("Nothing!");
    // } else {
    //     printf("Mask on? %s.\n", mask_on);
    // }
    if (mask_on == NULL || !is_mask_on(mask_on)) {
        puts("The computer must be wearing a mask to run this program.");
        return EXIT_FAILURE;
    }
    #ifndef DEBUG
    UD2(FUNC_DO_NOTHING);
    #endif
    // $ echo -n true | sha256sum
    // b5 be a4 1b 6c 62 3f 7c09f1bf24dcae58ebab3c0cdd90ad966bc43a45b44867e12b  -
    unsigned char *sha256_true = SHA256((const unsigned char *) mask_on, TRUE_LENGTH, NULL);
    // decrypt and assign values to capacities, current_amount, and correct_final_amount
    capacities[0] = (CAPACITY_1 ^ 0xb5) ^ sha256_true[0];
    capacities[1] = (CAPACITY_2 ^ 0xbe) ^ sha256_true[1];
    capacities[2] = (CAPACITY_3 ^ 0xa4) ^ sha256_true[2];
    current_amount[0] = (STARTING_AMOUNT_1 ^ 0x1b) ^ sha256_true[3];
    // current_amount[1] and current_amount[2] are zeros and this fact can be statically determined
    correct_final_amount[0] = (FINAL_AMOUNT_1 ^ 0x6c) ^ sha256_true[4];
    correct_final_amount[1] = (FINAL_AMOUNT_2 ^ 0x62) ^ sha256_true[5];
    correct_final_amount[2] = (FINAL_AMOUNT_3 ^ 0x3f) ^ sha256_true[6];
    #ifndef DEBUG
    entry();
    #else
        #ifdef REAL_PATH
            real_entry();
        #else
            fake_entry();
        #endif
    #endif
    return EXIT_SUCCESS;
}
