%global debug_package %{nil}

%define soversion 0
%define pkgname @NAME@

Name:           %{pkgname}
Version:        @VERSION@
Release:        @RELEASE@%{?dist}
Source:         %{pkgname}-%{version}.tar.gz
Summary:        World of Warships resource unpack tool & library
License:        MIT
URL:            https://github.com/wows-tools/wows-depack
BuildRoot:      %{_tmppath}/%{pkgname}-%{zone}-%{version}-%{release}-build
BuildRequires:  cmake
BuildRequires:  zlib-devel
BuildRequires:  pcre-devel
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  make

%description
wows-depack is a tool and library for unpacking World of Warships game resources.
It provides both a command-line interface and a C library for programmatic access.

%package cli
Summary:  Command-line interface for wows-depack
Requires: lib%{name}%{soversion} = %{version}-%{release}

%description cli
Command-line interface for the wows-depack library, allowing users to unpack
World of Warships game resources from the command line.

%package -n lib%{name}%{soversion}
Summary:  Library for unpacking World of Warships resources
Requires: zlib, pcre

%description -n lib%{name}%{soversion}
Shared library for unpacking World of Warships game resources.
This package contains the runtime library.

%package -n lib%{name}%{soversion}-devel
Summary:  Development files for wows-depack
Requires: lib%{name}%{soversion} = %{version}-%{release}

%description -n lib%{name}%{soversion}-devel
Development files for the wows-depack library, including header files
and documentation needed for developing applications that use wows-depack.


%prep
%setup -q

%build
%cmake -DCMAKE_SKIP_RPATH=TRUE
%cmake_build

%install
%cmake_install

%post -n lib%{name}%{soversion} -p /sbin/ldconfig
%postun -n lib%{name}%{soversion} -p /sbin/ldconfig

%files cli
%{_bindir}/wows-depack-cli

%files -n lib%{name}%{soversion}
%{_libdir}/libwows-depack.so*
%{_libdir}/libwows-depack.so

%files -n lib%{name}%{soversion}-devel
%{_includedir}/wows-depack.h

%changelog
* %(date "+%a %b %d %Y") Your Name <your.email@example.com> - %{version}-%{release}
- Initial package 
