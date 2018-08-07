SRCS=$(wildcard *.c)
SRCS+=$(wildcard scratchpad/*.c)
# Use .bin so that they can be added easily to .gitignore
TARGETS=$(SRCS:.c=.bin)
CFLAGS = -Wall -Wextra

all: $(TARGETS)

%.bin: %.c
	gcc $(CFLAGS) $< -o $@

.PHONY: run
run:
	@all_passed=true; \
	for f in `find . -iname '*.bin'`; do \
		printf "$$f -> "; \
		$$f || all_passed=false; \
	done; \
	$$all_passed && echo PASS || echo FAIL

clean:
	find . -iname '*.bin' -exec rm {} \;
