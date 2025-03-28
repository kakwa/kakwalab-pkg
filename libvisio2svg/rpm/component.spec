%define pkgname @NAME@

Name: %{pkgname}
Version: @VERSION@
Release: @RELEASE@%{?dist}
Source: %{pkgname}-%{version}.tar.gz
URL: @URL@
Vendor: @MAINTAINER@
License: @LICENSE@
Group: System/Servers
Summary: @SUMMARY@
BuildRoot: %{_tmppath}/%{pkgname}-%{zone}-%{version}-%{release}-build
BuildRequires: libemf2svg-devel, libwmf-devel, libxml2-devel, libvisio-devel, librevenge-devel, cmake, gcc, freetype-devel, gcc-c++
Requires: libemf2svg1, libwmf, libxml2, libvisio, librevenge

%description
@DESCRIPTION@

%package devel
Summary: @SUMMARY@, headers
%description devel
@DESCRIPTION@, headers

%package conv
Summary: @SUMMARY@, command line converter
%description conv
@DESCRIPTION@, command line converter

%prep
%setup -q -n %{pkgname}-%{version}

%build
%cmake -DCMAKE_SKIP_RPATH=TRUE
%cmake_build

%install
%cmake_install

%post -n %{pkgname} -p /sbin/ldconfig
%postun -n %{pkgname} -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
/usr/%{_lib}/*

%files devel
/usr/include/*

%files conv
%attr(755, root, root)/usr/bin/*

%changelog
* Wed Feb 01 2013 @MAINTAINER@ <@MAINTAINER_EMAIL@> 0.0.1-1
- initial Version
