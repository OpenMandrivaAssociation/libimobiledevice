%define major 6
%define libname %mklibname imobiledevice %{major}
%define devname %mklibname -d imobiledevice
%define _disable_ld_no_undefined 1

Summary:	Library for connecting to Apple iPhone and iPod touch
Name:		libimobiledevice
Version:	1.2.0
Release:	12
Group:		System/Libraries
License:	LGPLv2+
Url:		http://libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
Patch1:		344409e1d1ad917d377b256214c5411dda82e6b0...5a85432719fb3d18027d528f87d2a44b76fd3e12.patch
Patch2:		0001-userpref-GnuTLS-Fix-3.6.0-SHA1-compatibility.patch
Patch3:		0002-userpref-GnuTLS-Use-valid-serial-for-3.6.0.patch
BuildRequires:	python-cython
BuildRequires:	swig
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libplist)
BuildRequires:	pkgconfig(libplist++)
BuildRequires:	pkgconfig(libtasn1)
BuildRequires:	pkgconfig(libusbmuxd)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python3)

%description
libimobiledevice is a library for connecting
to Apple's iPhone or iPod touch devices

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for connecting to Apple iPhone and iPod touch

%description -n %{libname}
libimobiledevice is a library for connecting
to Apple's iPhone or iPod touch devices

%package -n %{devname}
Summary:	Development package for libimobiledevice
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Files for development with libimobiledevice.

%package -n python-imobiledevice
Summary:	Python bindings for libimobiledevice
Group:		Development/Python

%description -n python-imobiledevice
Python bindings for libimobiledevice.

%prep
%setup -q
%autopatch -p1

sed -i 's#1.3.21#2.0.0#g' configure

%build
%configure

%make -j1

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
%{_bindir}/idevicecrashreport
%{_bindir}/idevicename
%{_bindir}/idevicedebug
%{_bindir}/idevicenotificationproxy
%{_mandir}/man1/idevice*.1.*

%files -n %{libname}
%{_libdir}/libimobiledevice.so.%{major}*

%files -n %{devname}
%{_libdir}/pkgconfig/libimobiledevice-1.0.pc
%{_libdir}/libimobiledevice.so
%{_includedir}/libimobiledevice

%files -n python-imobiledevice
%{python_sitearch}/imobiledevice*
