%define major 6
%define api 1.0
%define libname %mklibname imobiledevice %{api} %{major}
%define devname %mklibname -d imobiledevice
%define _disable_ld_no_undefined 1

Summary:	Library for connecting to Apple iPhone and iPod touch
Name:		libimobiledevice
Version:	020210921
Release:	1
Group:		System/Libraries
License:	LGPLv2+
Url:		http://libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-20210921.tar.xz

BuildRequires:	swig
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libplist-2.0) >= 2.2.0
BuildRequires:	pkgconfig(libplist++-2.0) >= 2.2.0
BuildRequires:	pkgconfig(libtasn1)
BuildRequires:	pkgconfig(libusbmuxd-2.0) >= 2.0.2
BuildRequires:	pkgconfig(openssl)

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

%package -n %{name}-utilities
Group:		System Utilities
Summary:        Utilies for interrogating Apple devices
Requires:       %{libname} = %{version}-%{release}
%description -n %{name}-utilities
Utilities to interrogate Apple IOS devices 

%prep
%setup -q
%autopatch -p1 %{name}-20210921

%build
./autogen.sh
%configure --enable-openssl --without-cython

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
%{_mandir}/man1/idevice*.1.*

%files -n %{devname}
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/%{name}-%{api}.so
%{_includedir}/%{name}/
