%define major 3
%define libname %mklibname imobiledevice %{major}
%define develname %mklibname -d imobiledevice

Name:		libimobiledevice
Version:	1.1.4
Release:	1
Summary:	Library for connecting to Apple iPhone and iPod touch
Group:		System/Libraries
License:	LGPLv2+
URL:		http://libimobiledevice.org/
Source0:	http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2

BuildRequires:	libtasn1-devel
BuildRequires:	libplist-devel
BuildRequires:	usbmuxd-devel >= 1.0.8
BuildRequires:	glib2-devel
BuildRequires:	gnutls-devel
BuildRequires:	python-devel
BuildRequires:	swig
BuildRequires:	libplist++-devel

%description
libimobiledevice is a library for connecting
to Apple's iPhone or iPod touch devices

%package -n %{libname}
Group: System/Libraries
Summary: Library for connecting to Apple iPhone and iPod touch

%description -n %{libname}
libimobiledevice is a library for connecting
to Apple's iPhone or iPod touch devices

%package -n %{develname}
Summary: Development package for libimobiledevice
Group: Development/C
Provides: %{name}-devel = %{version}-%{release}
Requires: %{libname} = %{version}-%{release}

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
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%files
%doc AUTHORS COPYING.LESSER README
%{_bindir}/idevicebackup2
%{_bindir}/idevicedate
%{_bindir}/idevice_id
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
#%{python_sitearch}/imobiledevice*
