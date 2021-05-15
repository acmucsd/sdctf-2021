#include <stdio.h>
#include <stdlib.h>
#include <math.h>

unsigned int floorsqrt(unsigned int n) {
    if (n < 2)
        return n;

    unsigned int low = floorsqrt(n >> (unsigned int) 2) << (unsigned int) 1;
    unsigned int high = low + 1;
    return high * high > n ? low : high;
}

unsigned int ceilsqrt(unsigned int n) {
    return floorsqrt(n) + 1;
}

unsigned int* sieve_of_eratosthenes(int limit) {
    char *primality = malloc(limit * sizeof(char));

    // initialize entire array to true
    for (int i = 0; i < limit; i++)
        primality[i] = 1;

    // now, perform the sieve
    unsigned int small_limit = ceilsqrt(limit);
    for (int i = 2; i < small_limit; i++) {
        if(!primality[i])
            continue;
        for (int j = i*i; j < limit; j += i)
            primality[j] = 0;
    }

    unsigned int *primes = malloc(limit * sizeof(unsigned int));

    int j = 0;
    for (int i = 2; i < limit; i++) {
        if (primality[i])
            primes[j++] = i;
    }
    primes[j] = 0;

    free(primality);
    return primes;
}

unsigned int* sieve_of_eratosthenes2(int limit) {

    unsigned int segment_length = ceilsqrt(limit);

    // first find the lower sqrt N of primes
    unsigned int *first_primes = sieve_of_eratosthenes(segment_length);

    // allocate an array for all primes we might need to store
    int prime_amount = 0;
    unsigned int *primes = malloc(limit * sizeof(unsigned int));
    // store initial primes
    for(int i = 0; first_primes[i]; i++)
        primes[prime_amount++] = first_primes[i];

    // allocate a smaller array for the primality of the segment we're currently scanning
    char *primality = malloc(segment_length * sizeof(char));

    // process each segment
    unsigned int high = segment_length;
    for(unsigned int low = segment_length; low < limit; low += segment_length) {
        high += segment_length;
        if (high >= limit)
            high = limit;

        // initialize entire array to true
        for (int i = 0; i < segment_length; i++)
            primality[i] = 1;

        // scan this segment with our list of primes
        for (unsigned int i = 0; i < segment_length && first_primes[i]; i++) {
            unsigned int prime = first_primes[i];

            // starting number, the smallest number in the range that COULD have this prime as a factor
            unsigned int bottom = floor((double) low / (double) prime) * prime;

            if(bottom < low)
                bottom += prime;

            // mark multiples in the primality range
            for (unsigned int j = bottom; j < high; j += prime)
                primality[j - low] = 0;
        }

        // add new primes in segment to prime list
        for (unsigned int i = 0; i < segment_length; i++) {
            if (!primality[i])
                continue;
            primes[prime_amount++] = i + low;
        }
    }

    primes[prime_amount] = 0;

    free(primality);
    free(first_primes);

    return primes;
}

int main() {
    int canary = 0;
    char input[8];

    gets(input);

    if(canary) {
        printf("buffer overflow! sdctf{B3$T_0f-b0TH_w0rLds}");
        return 0;
    }

    char * end;
    const long amount = strtol(input, &end, 10);

    // shouldn't happen but important to prevent just in case
    if (amount <= 2 || amount > 99999999) {
        printf("number malformed");
        return 0;
    }

    unsigned int * primes = sieve_of_eratosthenes2(amount);
    for(int i = 0; i < amount; i++) {
        if(!primes[i]) {
            printf("There are exactly %d primes under %d", i, amount);
            return 0;
        }
    }
}
