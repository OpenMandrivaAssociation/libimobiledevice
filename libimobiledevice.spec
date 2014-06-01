%define major 4
%define libname %mklibname imobiledevice %{major}
%define devname %mklibname -d imobiledevice

Summary:	Library for connecting to Apple iPhone and iPod touch
Name:		libimobiledevice
Version:	1.1.6
Release:	12
Group:		System/Libraries
License:	LGPLv2+
Url:		http://libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2

BuildRequires:	python-cython python-plist
BuildRequires:	swig
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libplist)
BuildRequires:	pkgconfig(libplist++)
BuildRequires:	pkgconfig(libtasn1)
BuildRequires:	pkgconfig(libusbmuxd)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python)

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

sed -i 's#1.3.21#2.0.0#g' configure

%build
%configure \
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
%{_bindir}/idevicecrashreport
%{_bindir}/idevicename
%{_mandir}/man1/idevice*.1.*

%files -n %{libname}
%{_libdir}/libimobiledevice.so.%{major}*

%files -n %{devname}
%{_libdir}/pkgconfig/libimobiledevice-1.0.pc
%{_libdir}/libimobiledevice.so
%{_includedir}/libimobiledevice

%files -n python-imobiledevice
%{python_sitearch}/imobiledevice*
