%define name libimobiledevice
%define version 1.0.4
%define major 1
%define libname %mklibname imobiledevice %major
%define libnamedev %mklibname -d imobiledevice

Name:           %{name}
Version:        %{version}
Release:        %mkrel 1
Summary:        Library for connecting to Apple iPhone and iPod touch
Group:          System/Libraries
License:        LGPLv2+
URL:            http://libimobiledevice.org/
Source0:        http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libtasn1-devel
BuildRequires: libplist-devel
BuildRequires: usbmuxd-devel >= 0.1.4
BuildRequires: glib2-devel
BuildRequires: gnutls-devel
BuildRequires: python-devel

%description
libimobiledevice is a library for connecting to Apple's iPhone or iPod touch devices

%package -n %libname
Group: System/Libraries
Summary: Library for connecting to Apple iPhone and iPod touch
Requires: %name >= %version

%description -n %libname
libimobiledevice is a library for connecting to Apple's iPhone or iPod touch devices

%package -n %libnamedev
Summary: Development package for libimobiledevice
Group: Development/C
Provides: %name-devel = %version-%release
Requires: %libname = %{version}-%{release}

%description -n %libnamedev
Files for development with libimobiledevice.

%package -n python-imobiledevice
Summary: Python bindings for libimobiledevice
Group: Development/Python
BuildRequires: swig
BuildRequires: libplist++-devel
%py_requires -d


%description -n python-imobiledevice
Python bindings for libimobiledevice.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING.LESSER README
%{_bindir}/idevice_id
%{_bindir}/ideviceinfo
%{_bindir}/idevicepair
%{_bindir}/idevicesyslog
%{_bindir}/idevicebackup
%{_bindir}/ideviceimagemounter
%{_bindir}/idevicescreenshot
%{_mandir}/man1/idevice*.1.*

%files -n %libname
%defattr(-,root,root)
%_libdir/lib*.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libimobiledevice-1.0.pc
%{_libdir}/libimobiledevice.so
%{_libdir}/libimobiledevice*a
%{_includedir}/libimobiledevice

%files -n python-imobiledevice
%defattr(-,root,root,-)
%{python_sitearch}/imobiledevice/
