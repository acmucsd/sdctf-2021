CC = gcc
WARNINGS = -Werror=implicit-function-declaration -Wall -Wextra -Wformat=2 -Wconversion -Wduplicated-cond -Wlogical-op -Wshift-overflow=2 -Wfloat-equal -Wshadow
COMMON_DIR = ../../common/
COMMON_SRCS = $(COMMON_DIR)common.c
COMMON_HEADERS = $(COMMON_DIR)common.h

# _GNU_SOURCE enables Linux-specific signal handling for ud2 function calling
CFLAGS = -D_GNU_SOURCE $(WARNINGS) -I$(COMMON_DIR)

# -lcrypto: Link to OpenSSL crypto library for flag decryption, MD5, SHA256, etc.
LDLIBS = -lcrypto

all: 0xC0F1D debug-real.out debug-fake.out

# Challenge build (the version deployed to CTF participants)
0xC0F1D: cofid.c $(COMMON_SRCS) $(COMMON_HEADERS)
	$(CC) $(COMMON_SRCS) cofid.c $(LDLIBS) $(CFLAGS) -o 0xC0F1D
	strip 0xC0F1D

## Debug builds, to ease challenge author's testing, do not release to participants
# Real execution path
debug-real.out: cofid.c $(COMMON_SRCS) $(COMMON_HEADERS)
	$(CC) $(COMMON_SRCS) cofid.c $(LDLIBS) -g -DDEBUG -DREAL_PATH $(CFLAGS) -o debug-real.out

# Fake execution path
debug-fake.out: cofid.c $(COMMON_SRCS) $(COMMON_HEADERS)
	$(CC) $(COMMON_SRCS) cofid.c $(LDLIBS) -g -DDEBUG $(CFLAGS) -o debug-fake.out

.PHONY: clean all

clean:
	rm -f 0xC0F1D debug-real.out debug-fake.out

# Expect 2 fails in a row
# test-no-mask: debug-real.out
# 	./assert-fail.sh ./debug-real.out
# 	MASK_ON= ./assert-fail.sh ./debug-real.out
# 	MASK_ON=false ./assert-fail.sh ./debug-real.out
# 	MASK_ON=what ./assert-fail.sh ./debug-real.out
# 	MASK_ON=trueee ./assert-fail.sh ./debug-real.out
