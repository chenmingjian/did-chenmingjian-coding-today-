include ../Make.defines

src = $(wildcard *.c)
target = $(patsubst %.c, %, ${src})

.PHONY: all clean

all: ${target}

%:%.c
	$(CC) $(CFLAGS) -o $@ $< ${LIBS}


clean:
	rm -f ${target}
