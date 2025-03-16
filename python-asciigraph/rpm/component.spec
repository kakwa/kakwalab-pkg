%define pkgname @NAME@ 
%global modname asciigraph

Name: %{pkgname}
Summary: @SUMMARY@
Version: @VERSION@
Release: @RELEASE@%{?dist}
Source: %{pkgname}-%{version}.tar.gz
URL: @URL@ 
Vendor: @MAINTAINER@
License: @LICENSE@
Group: System/Servers
BuildArch: noarch


BuildRoot: %{_tmppath}/%{pkgname}-%{zone}-%{version}-%{release}-build


%description
@DESCRIPTION@

%package -n python2-%{modname}
Summary: @SUMMARY@, python 2
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

%description -n python2-%{modname}
@DESCRIPTION@, Python 2 version.


%package -n python3-%{modname}
Summary: @SUMMARY@, python 3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools, tree

%description -n python3-%{modname}
@DESCRIPTION@, Python 3 version.

%package -n %{modname}
Summary: @SUMMARY@, executable
Requires: python3-%{modname}

%description -n %{modname}
@DESCRIPTION@, Python 3 version.



%prep
%autosetup -n %{pkgname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%clean
rm -rf \$RPM_BUILD_ROOT

%files -n python2-%{modname}
%{python2_sitelib}/ascii_graph/
%{python2_sitelib}/ascii_graph-%{version}-*.egg-info/

%files -n python3-%{modname}
%{python3_sitelib}/ascii_graph/
%{python3_sitelib}/ascii_graph-%{version}-*.egg-info/


%files -n %{modname}
%attr(755,-,-)/usr/bin/asciigraph

%changelog
* Wed Feb 01 2013 @MAINTAINER@ <@MAINTAINER_EMAIL@> 0.0.1-1
- initial Version initiale
