CC = gcc
WARNINGS = -Wall -Wextra -Wformat=2 -Wconversion -Wduplicated-cond -Wlogical-op -Wshift-overflow=2 -Wfloat-equal -Wshadow
COMMON_DIR = ../../common/
COMMON_SRCS = $(COMMON_DIR)common.c
COMMON_HEADERS = $(COMMON_DIR)common.h

CFLAGS = $(WARNINGS) $(COMMON_SRCS) -I$(COMMON_DIR) -lm

# By convention: all excludes debug build to ease deployment
all: chal.out challenge/deploy.out

test-solve: solve.py chal.out
	python3 ./solve.py

# Debug build, to ease challenge author's testing, do not release to participants
debug.out: app-server.c $(COMMON_SRCS) $(COMMON_HEADERS)
	$(CC) app-server.c -g -DDEBUG $(CFLAGS) -o debug.out

# Deploy build (the deployed version)
challenge/deploy.out: app-server.c $(COMMON_SRCS) $(COMMON_HEADERS)
	$(CC) app-server.c -g -DDEPLOY $(CFLAGS) -o challenge/deploy.out

# Challenge build (the version given to CTF participants)
chal.out: app-server.c $(COMMON_SRCS) $(COMMON_HEADERS)
	$(CC) app-server.c $(CFLAGS) -o chal.out
	strip chal.out

.PHONY: clean run-debug run-chal

clean:
	rm -f chal.out debug.out challenge/deploy.out

run-debug: debug.out
	./debug.out

run-chal: chal.out
	./chal.out
