%define major 6
%define api 1.0
%define oldlibname %mklibname imobiledevice %{api} %{major}
%define libname %mklibname imobiledevice %{api}
%define devname %mklibname -d imobiledevice
%define _disable_ld_no_undefined 1

#define	git	20211124

Summary:	Library for connecting to Apple iPhone and iPod touch
Name:		libimobiledevice
Version:	1.3.0
Release:	%{?git:0.%{git}.}1
Group:		System/Libraries
License:	LGPLv2+
Url:		http://libimobiledevice.org/
Source0:	https://github.com/libimobiledevice/libimobiledevice/releases/download/%{version}/libimobiledevice-%{version}.tar.bz2
Patch0:		libimobiledevice-1.3.0-compile.patch

BuildRequires:	swig
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libplist-2.0) >= 2.3.0
BuildRequires:	pkgconfig(libplist++-2.0) >= 2.3.0
BuildRequires:	pkgconfig(libtasn1)
BuildRequires:	pkgconfig(libusbmuxd-2.0) >= 2.0.2
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libimobiledevice-glue-1.0)

%description
libimobiledevice is a library for connecting
to Apple's iPhone or iPod touch devices

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for connecting to Apple iPhone and iPod touch
%rename %{oldlibname}

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

%package -n %{name}-utilities
Group:		System Utilities
Summary:        Utilies for interrogating Apple devices
Requires:       %{libname} = %{version}-%{release}

%description -n %{name}-utilities
Utilities to interrogate Apple IOS devices 


%prep
%autosetup -p1
aclocal -I m4
autoheader
automake -a
autoconf

%configure --enable-openssl --without-cython

%build
%make_build

%install
%make_install

%files
%doc AUTHORS COPYING.LESSER

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}{,.*}

%files -n %{name}-utilities
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
%{_bindir}/idevicesetlocation
%{_mandir}/man1/idevice*.1*

%files -n %{devname}
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/%{name}-%{api}.so
%{_includedir}/%{name}/
