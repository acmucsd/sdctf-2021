#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LS_PATH "/bin/ls"

void not_allowed(const char *prog_name) {
    fprintf(stderr, "%s: Permission denied\n", prog_name);
    exit(1);
}

int main(int argc, char const *argv[]) {
    if (argc == 1) {
        // puts("only program name"); // debug
        return system(LS_PATH);
    } else if (argc > 2) {
        // not implemented, fake a permission error
        not_allowed(argv[0]);
    } else {
        // puts("more than it"); // debug
        if (!strcmp(argv[1], "bin/") || !strcmp(argv[1], "bin")) {
            return system(LS_PATH " bin/");
        } else if (!strcmp(argv[1], "opt/") || !strcmp(argv[1], "opt")) {
            // puts("faking it"); // debug
            // faked empty directory
            return 0;
        } else if (argv[1][0] == '-') {
            // seems like an option is provided
            not_allowed(argv[0]);
        } else {
            // Simulate fake permission denied output
            fprintf(stderr, "%s: cannot open directory '%s': Permission denied\n", argv[0], argv[1]);
            return 1;
        }
    }
}
