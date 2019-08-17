Name: libmodbus
Version: 3.0.8
Release: 1%{?dist}
Summary: A Modbus library
Group: Applications/System
License: LGPLv2+
URL: http://www.libmodbus.org/
Source0: https://github.com/downloads/stephane/libmodbus/libmodbus-%{version}.tar.gz
BuildRequires: autoconf, automake, libtool, xmlto, asciidoc

%description
libmodbus is a C library designed to provide a fast and robust implementation of
the Modbus protocol. It runs on Linux, Mac OS X, FreeBSD, QNX and Windows.

This package contains the libmodbus shared library.

%package devel
Summary: Development files for libmodbus
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
libmodbus is a C library designed to provide a fast and robust implementation of
the Modbus protocol. It runs on Linux, Mac OS X, FreeBSD, QNX and Windows.

This package contains libraries, header files and developer documentation needed
for developing software which uses the libmodbus library.

%prep
%setup -q

autoreconf

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)

%doc AUTHORS MIGRATION NEWS COPYING* README.rst

%{_libdir}/libmodbus.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/modbus/

%{_libdir}/pkgconfig/libmodbus.pc
%{_libdir}/libmodbus.so

%{_mandir}/man7/*.7.*
%{_mandir}/man3/*.3.*

%changelog
* Fri, 21 Feb 2014 Stéphane Raimbault <stephane.raimbault@gmail.com> - 3.0.6-1
- new upstream release

* Sun, 06 Oct 2013 Stéphane Raimbault <stephane.raimbault@gmail.com> - 3.0.5-1
- new upstream release

* Wed May 08 2013 Stéphane Raimbault <stephane.raimbault@gmail.com> - 3.0.4-1
- new upstream release

* Fri May 25 2012 Stéphane Raimbault <stephane.raimbault@gmail.com> - 3.0.3-1
- new upstream release

* Mon Jan 16 2012 Stéphane Raimbault <stephane.raimbault@gmail.com> - 3.0.2-1
- new upstream release

* Mon Jul 23 2011 Stéphane Raimbault <stephane.raimbault@gmail.com> - 3.0.1-2
- package reviewed by Peter Lemenkov <lemenkov@gmail.com> and Veeti Paananen
  <veeti.paananen@rojekti.fi> of Fedora Quality Assurance team

* Mon Jul 18 2011 Stéphane Raimbault <stephane.raimbault@gmail.com> - 3.0.1-1
- new upstream release

* Thu Jul 11 2011 Stéphane Raimbault <stephane.raimbault@gmail.com> - 3.0.0-1
- revert the license to LGPLv2.1+
- new spec file generated by autoconf
- add documentation, devel package and various changes

* Sun Jun 5 2011 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.9.4-1
- new upstream release

* Mon Jan 10 2011 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.9.3-1
- new upstream release

* Mon Oct 5 2010 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.9.2-1
- new upstream release

* Fri Jul 2 2008 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.0.1-1
- new upstream release

* Fri May 2 2008 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.0.0-1
- integrate extern_for_cpp in upstream.
- update the license to version LGPL v3.

* Tue Apr 30 2008 Todd Denniston <Todd.Denniston@ssa.crane.navy.mil> - 1.9.0-2
- get the license corrected in the spec file.
- add a URL for where to find libmodbus.
- tweak the summary and description.

* Tue Apr 29 2008 Todd Denniston <Todd.Denniston@ssa.crane.navy.mil> - 1.9.0-1
- upgrade to latest upstream (pre-release)
- port extern_for_cpp patch to 1.9.0

* Tue Apr 29 2008 Todd Denniston <Todd.Denniston@ssa.crane.navy.mil> - 1.2.4-2_tad
- add a patch to allow compiling with c++ code.

* Mon Apr 28 2008 Todd Denniston <Todd.Denniston@ssa.crane.navy.mil> - 1.2.4-1_tad
- build spec file.
- include patch for controling error-treat.
