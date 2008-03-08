all:
	@echo "all"

changelog:
	hg log --style=changelog > ChangeLog
