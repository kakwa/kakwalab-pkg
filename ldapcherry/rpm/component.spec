%define pkgname @NAME@
%define _unitdir /usr/lib/systemd/system/

Name: %{pkgname}
Version: @VERSION@
Release: @RELEASE@%{?dist}
Source: %{pkgname}-%{version}.tar.gz
Source1: ldapcherry 
Source2: ldapcherry.conf
Source3: ldapcherry.service
URL: @URL@ 
Vendor: @MAINTAINER@
License: @LICENSE@
Group: System/Servers
Summary: @SUMMARY@ 
BuildRoot: %{_tmppath}/%{pkgname}-%{zone}-%{version}-%{release}-build
BuildArch: noarch
Requires: python3-cherrypy, python3-ldap, python3-pyyaml, python3-mako, systemd
BuildRequires: python3-setuptools, python3-devel

%description
@DESCRIPTION@

%prep

%setup -q -n %{pkgname}-%{version}


%build
rm -rf $RPM_BUILD_ROOT
%py3_build

%install

%py3_install

mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/usr/lib/tmpfiles.d/
mkdir -p %{buildroot}/etc/sysconfig/
install -pm644 %{SOURCE1} %{buildroot}/etc/sysconfig/
install -pm644 %{SOURCE2} %{buildroot}/usr/lib/tmpfiles.d/
install -pm644 %{SOURCE3} %{buildroot}%{_unitdir}


%post
getent group ldapcherry >/dev/null || groupadd -r ldapcherry
getent passwd ldapcherry >/dev/null || \
    useradd -r -g ldapcherry -d /var/lib/ldapcherry -s /sbin/nologin \
    -c "LdapCherry daemon user" ldapcherry

systemd-tmpfiles --create /usr/lib/tmpfiles.d/ldapcherry.conf

systemctl daemon-reload

%preun
true

%clean
rm -rf \$RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/bin/ldapcherryd
/usr/share/ldapcherry/
/usr/lib/python*/site-packages/ldapcherry*
/usr/lib/systemd/system/ldapcherry.service
/usr/lib/tmpfiles.d/*
%config /etc/ldapcherry/*
%config /etc/sysconfig/ldapcherry

%changelog
* Wed Feb 01 2013 @MAINTAINER@ <@MAINTAINER_EMAIL@> 0.0.1-1
- initial Version initiale
