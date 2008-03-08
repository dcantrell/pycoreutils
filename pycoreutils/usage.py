#
# usage.py - pycoreutils --help screens for each command
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2.  This program is distributed in the
# hope that it will be useful, but WITHOUT ANY WARRANTY expressed or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.  You should have received a copy of the GNU General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
# USA. Any Red Hat trademarks that are incorporated in the source code or
# documentation are not subject to the GNU General Public License and may
# only be used or replicated with the express permission of Red Hat, Inc.
#
# Author: David Cantrell <dcantrell@redhat.com>
#

def pybasename_usage(cmd):
	print "Usage: %s NAME [SUFFIX]" % (cmd,)
	print "   or: %s OPTION" % (cmd,)
	print "Print NAME with any leading directory components removed."
	print "If specified, also remove a trailing SUFFIX.\n"
	print "      --help     display this help and exit"
	print "      --version  output version information and exit\n"
	print "Examples:"
	print "  %s /usr/bin/sort       Output \"sort\"." % (cmd,)
	print "  %s include/stdio.h .h  Output \"stdio\"." % (cmd,)

def pycksum_usage(cmd):
	print "Usage: %s [FILE]..." % (cmd,)
	print "   or: %s [OPTION]" % (cmd,)
	print "Print CRC checksum and byte counts of each FILE.\n"
	print "      --help     display this help and exit"
	print "      --version  output version information and exit"

def pydirname_usage(cmd):
	print "Usage: %s NAME" % (cmd,)
	print "   or: %s OPTION" % (cmd,)
	print "Print NAME with its trailing /component removed; if NAME contains no /'s,"
	print "output `.' (meaning the current directory).\n"
	print "      --help     display this help and exit"
	print "      --version  output version information and exit\n"
	print "Examples:"
	print "  %s /usr/bin/sort  Output \"/usr/bin\"." % (cmd,)
	print "  %s stdio.h        Output \".\"." % (cmd,)

def pygroups_usage(cmd):
	print "Usage: %s [OPTIONS]... [USERNAME]..n" % (cmd,)
	print "      --help     display this help and exit"
	print "      --version  output version information and exit\n"
	print "Same as id -Gn.  If no USERNAME, user current process."

def pyhostid_usage(cmd):
	print "Usage: %s" % (cmd,)
	print "   or: %s OPTION" % (cmd,)
	print "Print the numeric identifier (in hexadecimal) for the current host.\n"
	print "      --help     display this help and exit"
	print "      --version  output version information and exit"

def pylogname_usage(cmd):
	print "Usage: %s [OPTION]..." % (cmd,)
	print "Print the name of the current user.\n"
	print "     --help      display this help and exit"
	print "     --version   output version information and exit"

def pymkdir_usage(cmd):
	print "Usage: %s [OPTION] DIRECTORY..." % (cmd,)
	print "Create the DIRECTORY(ies), if they do not already exist.\n"
	print "      -m, --mode=MODE"
	print "                 set permission mode (as in chmod), not rwxrwxrwx - umask"
	print "      -p, --parents"
	print "                 no error if existing, make parent directories as needed"
	print "      -v, --verbose"
	print "                 print a message for each created directory"
	print "      --help     display this help and exit"
	print "      --version  output version information and exit"

def pyprintenv_usage(cmd):
	print "Usage: %s [VARIABLE]..." % (cmd,)
	print "   or: %s OPTION" % (cmd,)
	print "If no environment VARIABLE specified, print them all.\n"
	print "      --help     display this help and exit"
	print "      --version  output version information and exit\n"
	print "NOTE: your shell may have its own version of printenv, which usually supercedes"
	print "the version described here.  Please refer to your shell's documentation"
	print "for details about the options it supports."

def pypwd_usage(cmd):
	print "Usage: %s [OPTION]" % (cmd,)
	print "Print the full filename of the current working directory.\n"
	print "      --help     display this help and exit"
	print "      --version  output version information and exit\n"
	print "NOTE: your shell may have its own version of pwd, which usually supercedes"
	print "the version described here.  Please refer to your shell's documentation"
	print "for details about the options it supports."

def pysleep_usage(cmd):
	print "Usage: %s NUMBER[SUFFIX]..." % (cmd,)
	print "   or: %s OPTION" % (cmd,)
	print "Pause for NUMBER seconds.  SUFFIX may be `s' for seconds (the default),"
	print "`m' for minutes, `h' for hours, or `d' for days.  Unlink most implementations"
	print "that require NUMBER be an integer, here NUMBER may be an arbitrary floating"
	print "point number.\n"
	print "      --help     display this help and exit"
	print "      --version  output version information and exit"

def pysync_usage(cmd):
	print "Usage: %s [OPTION]" % (cmd,)
	print "Force changed blocks to disk, update the super block.\n"
	print "      --help     display this help and exit"
	print "      --version  output version information and exit"

def pytee_usage(cmd):
	print "Usage: %s [OPTION]... [FILE]..." % (cmd,)
	print "Copy standard input to each FILE, and also to standard output.\n"
	print "      -a, --append"
	print "                 append to the given FILEs, do not overwrite"
	print "      -i, --ignore-interrupts"
	print "                 ignore interrupt signals"
	print "      --help     display this help and exit"
	print "      --version  output version information and exit"

def pytty_usage(cmd):
	print "Usage: %s [OPTION]..." % (cmd,)
	print "Print the file name of the terminal connected to standard input.\n"
	print "  -s, --silent, --quiet   print nothing, only return an exit status"
	print "      --help     display this help and exit"
	print "      --version  output version information and exit"

def pyuname_usage(cmd):
	print "Usage: %s [OPTION]..." % (cmd,)
	print "Print certain system information.  With no OPTION, same as -s.\n"
	print "  -a, --all                print all information, in the following order,"
	print "                             except omit -p and -i if unknown:"
	print "  -s, --kernel-name        print the kernel name"
	print "  -n, --nodename           print the network node hostname"
	print "  -r, --kernel-release     print the kernel release"
	print "  -v, --kernel-version     print the kernel version"
	print "  -m, --machine            print the machine hardware name"
	print "  -p, --processor          print the processor type or \"unknown\""
	print "  -i, --hardware-platform  print the hardware platform or \"unknown\""
	print "  -o, --operating-system   print the operating system"
	print "      --help     display this help and exit"
	print "      --version  output version information and exit"

def pywhoami_usage(cmd):
	print "Usage: %s [OPTION]..." % (cmd,)
	print "Print the user name associated with the current effective user ID."
	print "Same as id -un.\n"
	print "     --help      display this help and exit"
	print "     --version   output version information and exit"

def pyyes_usage(cmd):
	print "Usage: %s [STRING]..." % (cmd,)
	print "   or: %s OPTION" % (cmd,)
	print "Repeatedly output a line with all specified STRING(s), or `y'.\n"
	print "      --help     display this help and exit"
	print "      --version  output version information and exit"
