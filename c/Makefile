SRCS=$(wildcard *.c)
# Use .bin so that they can be added easily to .gitignore
TARGETS=$(SRCS:.c=.bin)
CFLAGS = -Wall -Wextra

all: $(TARGETS)

%.bin: %.c
	gcc $(CFLAGS) $< -o $@

clean:
	rm *.bin
