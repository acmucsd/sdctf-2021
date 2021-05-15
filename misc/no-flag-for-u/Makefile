WARNINGS = -Wall -Wextra -Wformat=2 -Wconversion -Wduplicated-cond -Wlogical-op -Wshift-overflow=2 -Wfloat-equal -Wshadow
# Everything is statically linked to prevent environment variable LD_* attacks
CFLAGS = $(WARNINGS) -static
RUNDIR = challenge/run

all: $(RUNDIR)/bin/cat $(RUNDIR)/bin/ls

$(RUNDIR)/bin/cat: cat.c
	cc cat.c $(CFLAGS) -o $(RUNDIR)/bin/cat

$(RUNDIR)/bin/ls: ls.c
	cc ls.c $(CFLAGS) -o $(RUNDIR)/bin/ls

clean:
	rm -f $(RUNDIR)/bin/cat $(RUNDIR)/bin/ls

.PHONY: all
