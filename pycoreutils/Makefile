#
# Makefile for pycoreutils modules written in C
#

# Python variables
PYVER  = $(shell python -c 'import sys; print sys.version[0:3]')
PYTHON = python$(PYVER)
PYINC  = $(shell python -c 'from distutils.sysconfig import get_python_inc; print get_python_inc()')

# Operating system
OS     = $(shell uname)

# Compiler flags and settings
CC     ?= gcc
CFLAGS += -I$(PYINC)

# Host-specific build flags
ifeq ($(OS), Darwin)
CFLAGS  += -arch i386 -arch ppc -DPIC
LDFLAGS += -flat_namespace -undefined suppress -bundle -arch i386 -arch ppc
endif

ifeq ($(OS), Linux)
CFLAGS  += -fPIC
LDFLAGS += -shared -g -fPIC
endif

# Modules to build
PYMODULES = pycoreutilsmodule.so

all: $(PYMODULES)

%.o: %.c
	$(CC) -c $(CFLAGS) -o $@ $<

%.so: %.o
	$(CC) $(LDFLAGS) -o $@ $< $(LDFLAGS)

clean:
	rm -f *.o *.so *.lo *.pyc
