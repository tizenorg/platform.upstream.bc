Name:           bc
BuildRequires:  automake bison ed flex readline-devel
Url:            ftp://ftp.gnu.org/pub/gnu/bc
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
Version:        1.06
Release:        0
Summary:        GNU Command Line Calculator
Source:         %{name}-%{version}.tar.bz2

%description
bc is an interpreter that supports numbers of arbitrary precision and
the interactive execution of statements. The syntax has some
similarities to the C programming language. A standard math library is
available through command line options. When used, the math library is
read in before any other input files. bc then reads in all other files
from the command line, evaluating their contents. Then bc reads from
standard input (usually the keyboard).

The dc program is also included. dc is a calculator that supports
reverse-polish notation and allows unlimited precision arithmetic.
Macros can also be defined. Normally, dc reads from standard input but
can also read in files specified on the command line. A calculator with
reverse-polish notation saves numbers to a stack. Arguments to
mathematical operations (operands) are "pushed" onto the stack until
the next operator is read in, which "pops" its arguments off the stack
and "pushes" its results back onto the stack.

%prep
%setup -q

%build
autoreconf -fi
./configure CFLAGS="$RPM_OPT_FLAGS" \
            --with-readline \
            --prefix=/usr \
	    --infodir=%{_infodir} \
            --mandir=%{_mandir} \
            --build=%{_target_cpu}-suse-linux
rm bc/libmath.h
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
/usr/bin/bc
/usr/bin/dc
%{_infodir}/*.info*
%{_mandir}/man1/*

%changelog