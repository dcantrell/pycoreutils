#
# Makefile for pycoreutils modules written in C
#

# Python variables
PYVER         = $(shell python -c 'import sys; print sys.version[0:3]')
PYTHON        = python$(PYVER)
PYTHONINCLUDE = /usr/include/$(PYTHON)

# Compiler flags and settings
CC     ?= gcc
CFLAGS += -I$(PYTHONINCLUDE)

# Modules to build
PYMODULES = pycoreutilsmodule.c

all: $(PYMODULES)

%.lo: %.c
	$(CC) -c $(CFLAGS) -fPIC -o $@ $<

%.so: %.lo
	$(CC) -shared -g -fPIC -o $@ $< $(LDFLAGS)

clean:
	rm -f *.o *.so *.lo *.pyc
