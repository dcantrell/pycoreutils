PKG     = pycoreutils
VER     = 0.1

REPO    = https://pycoreutils.googlecode.com/svn

DESTDIR = /usr/local

all:
	@echo "Available targets:"
	@echo "    changelog    Generate new ChangeLog"
	@echo "    install      Install pycoreutils to target directories"
	@echo "    tag          Tag repository as v$(VER)"
	@echo "    dist-gzip    Generate a release archive ($(PKG)-$(VER).tar.gz)"
	@echo "    release      Perform 'make tag && make dist-gzip'"

changelog:
	svn log > ChangeLog

install:
	@echo "WRITEME"

tag:
	@echo "WRITEME"

dist-gzip:
	@echo "WRITEME"

release:
	@echo "WRITEME"

clean:
	-rm -rf $(PKG)-$(VER) $(PKG)-$(VER).tar.gz
