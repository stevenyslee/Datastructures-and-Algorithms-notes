CC=gcc
CFLAGS = -std=c11 -Wall -pedantic
DCFLAGS = -std=c99 -Wall -pedantic -DDEBUG=1
.PHONY: clean
SRC_FILES := $(wildcard src/*.c)

DEBUG_FILES = src/*.c


debug : build_deb
	$(CC) ./obj/debug.o -o ./debug $(DCFLAGS)

run_test: debug
	./debug

run_valgrind: debug
	valgrind ./debug

build_deb: src/bst.c
	@mkdir -p ./obj/
	$(CC) src/bst.c -c -o ./obj/debug.o $(DCFLAGS)
