#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CAT_PATH "/bin/cat"
#define README_PATH "README"

int main(int argc, char const *argv[]) {
    if (argc == 2 && !strcmp(argv[1], README_PATH)) {
        return system(CAT_PATH " " README_PATH);
    }
    puts("No flag for you!");
    return 0;
}
