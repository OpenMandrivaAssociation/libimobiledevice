%define major 4
%define libname %mklibname imobiledevice %{major}
%define develname %mklibname -d imobiledevice

Name:		libimobiledevice
Version:	1.1.5
Release:	1
Summary:	Library for connecting to Apple iPhone and iPod touch
Group:		System/Libraries
License:	LGPLv2+
URL:		http://libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(libtasn1)
BuildRequires:	pkgconfig(libplist)
BuildRequires:	pkgconfig(libplist++)
BuildRequires:	pkgconfig(libusbmuxd)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	python-devel
BuildRequires:	python-cython
BuildRequires:	swig

%description
libimobiledevice is a library for connecting
to Apple's iPhone or iPod touch devices

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for connecting to Apple iPhone and iPod touch
Obsoletes:	%{mklibname imobiledevice 2} <= 1.1.1

%description -n %{libname}
libimobiledevice is a library for connecting
to Apple's iPhone or iPod touch devices

%package -n %{develname}
Summary:	Development package for libimobiledevice
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
Files for development with libimobiledevice.

%package -n python-imobiledevice
Summary: Python bindings for libimobiledevice
Group: Development/Python
%py_requires -d

%description -n python-imobiledevice
Python bindings for libimobiledevice.

%prep
%setup -q
sed -i 's#1.3.21#2.0.0#g' configure

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING.LESSER README
%{_bindir}/idevicebackup2
%{_bindir}/idevicedate
%{_bindir}/idevice_id
%{_bindir}/idevicedebugserverproxy
%{_bindir}/idevicediagnostics
%{_bindir}/ideviceprovision
%{_bindir}/ideviceinfo
%{_bindir}/idevicepair
%{_bindir}/ideviceenterrecovery
%{_bindir}/idevicesyslog
%{_bindir}/idevicebackup
%{_bindir}/ideviceimagemounter
%{_bindir}/idevicescreenshot
%{_mandir}/man1/idevice*.1.*

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_libdir}/pkgconfig/libimobiledevice-1.0.pc
%{_libdir}/libimobiledevice.so
%{_includedir}/libimobiledevice

%files -n python-imobiledevice
%{python_sitearch}/imobiledevice*


%changelog
* Tue Apr 17 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.4-1
+ Revision: 791424
- BR:pkgconfig(openssl)
- version update 1.1.4
- descr line too long
- rpmlint fixes
- version update 1.1.2

* Sun Dec 04 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.1-1
+ Revision: 737562
- update files list
- reapply swig fix
- new major 2
- new 1.1.1 unstable version
- fixes build for swig > 2.0
- added patches for iOS5
- added patch for gnutls 2.2.0 (disabled)

* Sat Dec 03 2011 Zé <ze@mandriva.org> 1.0.6-3
+ Revision: 737425
- fix python bindings build

  + Matthew Dawkins <mattydaw@mandriva.org>
    - rebuild
    - cleaned up spec
    - remove BuildRoot, mkrel, clean section, defattr
    - removed .la files
    - disabled static build
    - removed old ldconfig scriptlets
    - remove dep LOOP

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-2
+ Revision: 662378
- mass rebuild

* Tue Apr 05 2011 Funda Wang <fwang@mandriva.org> 1.0.6-1
+ Revision: 650567
- new version 1.0.6

  + Matthew Dawkins <mattydaw@mandriva.org>
    - removed poorly commented out patch

* Sun Nov 28 2010 Funda Wang <fwang@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 602231
- new version 1.0.4

* Mon Nov 01 2010 Funda Wang <fwang@mandriva.org> 1.0.2-3mdv2011.0
+ Revision: 591447
- rebuild for py 2.7

* Thu Jul 22 2010 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-1mdv2011.0
+ Revision: 556904
- libimobiledevice 1.0.2

* Fri May 14 2010 Christophe Fergeau <cfergeau@mandriva.com> 1.0.1-1mdv2010.1
+ Revision: 544746
- 1.0.1

* Mon Mar 22 2010 Christophe Fergeau <cfergeau@mandriva.com> 1.0.0-1mdv2010.1
+ Revision: 526320
- libimobiledevice 1.0.0
- new major (0 => 1)

* Mon Feb 01 2010 Christophe Fergeau <cfergeau@mandriva.com> 0.9.7-1mdv2010.1
+ Revision: 499151
- import libimobiledevice

