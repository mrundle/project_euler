SRCS=$(wildcard *.c)
# Use .bin so that they can be added easily to .gitignore
TARGETS=$(SRCS:.c=.bin)
CFLAGS = -Wall -Wextra

all: $(TARGETS)

%.bin: %.c
	gcc $(CFLAGS) $< -o $@

.PHONY: run
run:
	@for f in `find . -iname '*.bin'`; do echo -n $$f '-> '; $$f; done

clean:
	rm *.bin
