#include <stdio.h>
#include <stdint.h>
#include <limits.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <math.h>
#include <unistd.h>
#include <inttypes.h>

// #define DEBUG // To enable debug messages that should not be shown to the CTF participant

#include "common.h"

// Buffer limits start
#define NAME_MAX_LENGTH 250
#define FIRSTNAME_MAX_LENGTH 100
#define LASTNAME_MAX_LENGTH 100
#define PID_DIGIT_COUNT 8
#define PID_LENGTH (PID_DIGIT_COUNT + 1)
#define FLAG_MAX_LENGTH 256
// Buffer limits end

#define TIME_DIVISOR 4
#define HASH_PRIME 31

// PID_STRING[78] = 'H'
// PID format: H########
#define PID_STRING "ONCE UPON A TIME THERE USED TO BE A FAMILY OF DRAGONS. ONE OF THEM IS CALLED GHIDRA, AND THE OTHER IS CALLED..."

// decrypted text: yeet
#define YEET_ENCRYPTED "6)bc"
#define YEET_LENGTH 4

#define FLAG_FILENAME "flag.txt"

#define ACCEPTANCE_COUNT 10

// 2**64
#define APPLICANT_COUNT_STR "18446744073709551616"

uint64_t time_seed;
char lastname[LASTNAME_MAX_LENGTH];
char firstname[FIRSTNAME_MAX_LENGTH];
char student_id[PID_LENGTH+1];

char get_first_pid_letter(void) {
    // Use volatile qualifiers to prevent -O0 optimization from making this too easy
    // volatile int ternary_digits[] = {2, 2, 0, 1};
    volatile int ternary_digits[] = {1, 0, 2, 2};
    volatile int index=0;
    volatile double three = 3.0;
    volatile double four = 4.0;
    for (int i=0; i<(int)(sizeof(ternary_digits)/sizeof(int)); i++) {
        index += ternary_digits[i] * (int) round(pow(3.0, i));
    }
    index += (int) round(sqrt(pow(three, 2) + pow(four, 2)));
    // int index = (int) round(2 * pow(3.0, 3) + 2 * pow(3.0, 2) + 1 * pow(3.0, 0) + sqrt(pow(3.0, 2) + pow(4.0, 2)));
    return PID_STRING[index];
}

void srand_name(void) {
    unsigned int hash=0;
    size_t firstname_length = strlen(firstname), lastname_length = strlen(lastname);
    // Hash strings
    for (size_t i=0; i<firstname_length; i++) {
        hash *= HASH_PRIME;
        hash += (unsigned char) firstname[i];
    }
    for (size_t i=0; i<lastname_length; i++) {
        hash *= HASH_PRIME;
        hash += (unsigned char) lastname[i];
    }
    srand(hash);
}

void seed_with_time(void) {
    time_seed = ((uint64_t) time(NULL)) / TIME_DIVISOR;
}

void header(void) {
    puts("Welcome to the UCSD capped major application for the department of Redstone and Computer Science (RCE).\n"
        "Your prospective major: Computer Science.\n"
        "Note that Computer Science is a very competitive major, which means that you must be prepared to consider an alternate major.\n"
        "Note that admission decision is based *solely* on a lottery system provided that you meet the minimum requirements.\n\n"

        "Disclaimer: Similarity of this application with the CSE capped admission program from University of California San Diego is purely accidental.\n"
        "Always refer to information on https://cse.ucsd.edu/undergraduate/cse-capped-admissions-program for that application\n\n"

        "Please answer a series of question below:\n");
}

#define NAME_DELIMITER ", "

void invalid_name(void) {
    puts("Invalid name!");
    die();
}

void get_name(void) {
    char full_name[NAME_MAX_LENGTH];
    char *tmp_firstname, *tmp_lastname;
    // printf("1. Name (format: `Last, First`, no quotes): ");
    printf("1. Name (Last, First): ");
    read_input(full_name, NAME_MAX_LENGTH);
    // puts(full_name); // DEBUG
    tmp_lastname = strtok(full_name, NAME_DELIMITER);
    tmp_firstname = strtok(NULL, NAME_DELIMITER);
    if (tmp_firstname == NULL || tmp_lastname == NULL) {
        MSG_DEBUG("Name has too few tokens!");
        invalid_name();
    }
    // More tokens
    if (strtok(NULL, NAME_DELIMITER) != NULL) {
        MSG_DEBUG("Name has too many tokens!");
        invalid_name();
    }
    // DEBUG:
    // puts(tmp_firstname);
    // puts(tmp_lastname);
    // TOOD: only allow names from a restricted list
    if (strlen(tmp_firstname) >= FIRSTNAME_MAX_LENGTH || strlen(tmp_lastname) >= LASTNAME_MAX_LENGTH) {
        MSG_DEBUG("One part of the name is too long!");
        invalid_name();
    }
    strncpy(firstname, tmp_firstname, FIRSTNAME_MAX_LENGTH);
    strncpy(lastname, tmp_lastname, LASTNAME_MAX_LENGTH);
}

void print_pid_debug(void) {
    #ifdef DEBUG
    printf("Name (First Last): %s %s\n", firstname, lastname);
    srand_name();
    printf("%c%08d\n", get_first_pid_letter(), rand() % 100000000);
    #endif
}

void invalid_student_id(void) {
    printf("Invalid student ID, you are pretending to be %s %s right?\n"
        "Get out of here hacker!\n", firstname, lastname);
    die();
}

void check_pid(void) {
    char user_input_id[PID_LENGTH+1];
    long pid_num;
    // char *endptr=NULL;
    char *endptr;
    printf("2. Student ID: ");
    // LLONG_MAX has greater than 8 digits so it's fine with gcc
    fflush(stdout);
    for (int i=0; i<PID_LENGTH; i++) {
        if ((user_input_id[i] = ck_getchar()) == '\n') {
            MSG_DEBUG("Too few characters in student ID!");
            invalid_student_id();
        }
    }
    if (ck_getchar() != '\n') {
        MSG_DEBUG("Too many characters in student ID!");
        invalid_student_id();
    }
    user_input_id[PID_LENGTH] = '\0'; // to terminate the string
    // printf("Entered student ID is %s\n", user_input_id); // DEBUG
    if (user_input_id[0] != get_first_pid_letter()) {
        MSG_DEBUG("First letter of student ID incorrect!");
        invalid_student_id();
    }
    // read_input(user_input_id + 1, PID_DIGIT_COUNT);
    pid_num = strtol(user_input_id + 1, &endptr, 10);
    // if (endptr != NULL) {
    //     MSG_DEBUG("Invalid characters detected in the numeric part of student ID");
    //     invalid_student_id();
    // }
    if (endptr != user_input_id + PID_LENGTH) {
        MSG_DEBUG("Invalid characters detected in the numeric part of student ID");
        invalid_student_id();
    }
    // if (pid_num == LONG_MAX || pid_num == LONG_MIN) {
    //     MSG_DEBUG("Overflow or underflow in student ID digits!");
    //     invalid_student_id();
    // }
    if (pid_num < 0) {
        MSG_DEBUG("Negative student ID!");
        invalid_student_id();
    }
    srand_name();
    if (pid_num != (rand() % 100000000)) {
        MSG_DEBUG("Incorrect numeric part of student ID!");
        invalid_student_id();
    }
}

void submission_confirmation(void) {
    char buf[YEET_LENGTH+1];
    memset(buf, (int) '\0', YEET_LENGTH); // initialize the entire memory region
    puts("\nAre you ready to submit your application?");
    read_input(buf, YEET_LENGTH+1);
    // encrypt buf in place
    for (int i=0; i<YEET_LENGTH; i++) {
        buf[i] = (char) ((buf[i] ^ (PID_STRING[i] - i*i)) + i*i*i);
    }
    // encrypt buf in place end
    if (!timing_safe_equal(buf, YEET_ENCRYPTED, YEET_LENGTH)) {
        puts("Not getting an affirmative response (subjectively determined). Application canceled. :(");
        die();
    }
}

// void print_flag(void) {
//     char flag_buffer[FLAG_MAX_LENGTH];
//     FILE *flag_file = fopen(FLAG_FILENAME, "r");
//     if (flag_file == NULL) {
//         PERROR_FATAL("print_flag: Failed to read flag");
//     }
//     fgets(flag_buffer, FLAG_MAX_LENGTH, flag_file);
//     if (fclose(flag_file) == EOF) {
//         PERROR_FATAL("print_flag: Failed to close flag file");
//     }
//     puts(flag_buffer);
// }

uint32_t rand32(uint32_t seed) {
    // Assume RAND_MAX is INT_MAX: 2^31 - 1
    srand(seed);
    return (uint32_t) rand();
}

uint64_t rand64(uint64_t seed) {
    uint32_t r1 = rand32((uint32_t) (seed >> 32));
    uint32_t r2 = rand32((uint32_t) seed);
    return (((uint64_t) r2) << 32) + r1;
}

uint64_t hash64_name(void) {
    uint64_t hash=0xc0de5bad13375eedULL;
    size_t firstname_length = strlen(firstname), lastname_length = strlen(lastname);
    // Hash strings
    for (size_t i=0; i<firstname_length; i++) {
        hash *= HASH_PRIME;
        hash += (unsigned char) firstname[i];
    }
    for (size_t i=0; i<lastname_length; i++) {
        hash *= HASH_PRIME;
        hash += (unsigned char) lastname[i];
    }
    return hash;
    // return time_seed; // expected return value
}

#define RANK_MSG(rank) "Your randomly assigned rank in the lottery: " rank "/" APPLICANT_COUNT_STR ". Top %.2f%%.\n"

int run_lottery(void) {
    // printf("debug: %" PRIu64 ",%" PRIu64 "\n", rand64(time_seed), rand64(hash64_name()));
    uint64_t standing = rand64(time_seed) - rand64(hash64_name());
    // basically require time_seed == hash64_name()
    uint64_t place = standing + 1; // place
    // printf("Your randomly assigned rank in the lottery: %" PRIu64 "/" APPLICANT_COUNT_STR ". Top %.2d%%.\n", place, place * 100.0 / ((double) UINT64_MAX + 1.0));
    if (place == 0) {
        // Undeflow, standing is UINT64_MAX
        printf(RANK_MSG(APPLICANT_COUNT_STR), 100.0);
    } else {
        printf(RANK_MSG("%" PRIu64), place, (double) place * 100 / ((double) UINT64_MAX + 1.0));
    }
    return standing < (uint64_t) ACCEPTANCE_COUNT; // win if standing is 0..9
}

void application_result(void) {
    // Lottery machine (based on LCG, which is easily reversible once you are able to compute the modular multiplicative inverse)
    // print_flag();
    if (run_lottery()) {
        // Win!!!
        char flag_buffer[FLAG_MAX_LENGTH];
        FILE *flag_file = fopen(FLAG_FILENAME, "r");
        if (flag_file == NULL) {
            PERROR_FATAL("print_flag: Failed to open flag");
        }
        if (fgets(flag_buffer, FLAG_MAX_LENGTH, flag_file) == NULL) {
            PERROR_FATAL("print_flag: Failed to read flag");
        }
        if (fclose(flag_file) == EOF) {
            PERROR_FATAL("print_flag: Failed to close flag file");
        }
        printf(
            "Dear %s %s,\n\n"

            "Congratulations on your admission to the department of RCE\n"
            "Your Major: Computer Science.\n"
            "Here's the flag:\n"
            "%s\n" // flag_buffer already has a \n at the end

            "Best wishes,\n"
            "Kevin He\n"
            "Chancellor\n",
        firstname, lastname, flag_buffer);
    } else {
        printf(
            "Dear %s %s,\n\n"

            "Thank you for applying to the department of RCE.\n"
            "We are sorry that we could not offer you a spot.\n"
            "There are " APPLICANT_COUNT_STR " total applicants this quarter and\n"
            "we could only offer spots to %d of them.\n\n"

            "Best wishes,\n"
            "Kevin He\n"
            "Chancellor\n",
        firstname, lastname, ACCEPTANCE_COUNT);
    }
}

int main(void) {
    seed_with_time();
    header();
    get_name();
    print_pid_debug(); // DEBUG
    check_pid();
    submission_confirmation();
    puts("Submitting application. Please wait...\n");
    fflush(stdout);
    sleep(1);

    // seed_with_time();
    application_result();
    return EXIT_SUCCESS;
}
