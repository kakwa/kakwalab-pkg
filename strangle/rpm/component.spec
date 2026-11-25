%define pkgname @NAME@
%define _unitdir /usr/lib/systemd/system/

%global debug_package %{nil}

Name:      %{pkgname}
Version:   @VERSION@
Release:   @RELEASE@%{?dist}
Source:    %{pkgname}-%{version}.tar.gz
Source1:   strangle-server.service
Source2:   server.yml
Source3:   collection.yml

URL:       @URL@
Vendor:    @MAINTAINER@
License:   @LICENSE@
Group:     System/Servers
Summary:   @SUMMARY@
BuildRoot: %{_tmppath}/%{pkgname}-%{_build_arch}-%{version}-%{release}-build

BuildRequires: golang >= 1.27
BuildRequires: python3-devel
BuildRequires: pkgconf-pkg-config
BuildRequires: nodejs
BuildRequires: npm
BuildRequires: ansible
BuildRequires: systemd-rpm-macros
Requires:      ansible
Requires:      python3
Requires:      systemd
Requires:      shadow-utils

%description
@DESCRIPTION@

This package provides the strangle server, its worker subcommand, a systemd
service running as the strangle user, configuration in /etc/strangle and a
checkout directory in /var/lib/strangle.

%prep
%setup -q -n %{pkgname}-%{version}

%build
export GOPROXY=https://proxy.golang.org
export GOSUMDB=sum.golang.org
export GO111MODULE=on
export GOTOOLCHAIN=auto
export LANG=C.UTF-8
export LC_ALL=C.UTF-8
export HOME=%{_builddir}
export PKG_CONFIG=%{_builddir}/scripts/pkg-config-cpy

(cd web && npm ci --no-audit --no-fund && npm run build)
go build -ldflags="-s -w" -o strangle ./cmd/strangle

%check
export GOPROXY=https://proxy.golang.org
export GOSUMDB=sum.golang.org
export GO111MODULE=on
export GOTOOLCHAIN=auto
export LANG=C.UTF-8
export LC_ALL=C.UTF-8
export HOME=%{_builddir}
export ANSIBLE_REMOTE_TMP=/tmp/.ansible/tmp

go test ./...

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_unitdir}
install -d %{buildroot}%{_sysconfdir}/strangle
install -d %{buildroot}%{_sharedstatedir}/strangle
install -d %{buildroot}%{_datadir}/doc/%{pkgname}/examples/demo

install -m 755 strangle %{buildroot}%{_bindir}/strangle
install -pm 644 %{SOURCE1} %{buildroot}%{_unitdir}/strangle-server.service
install -pm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/strangle/server.yml
install -pm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/strangle/collection.yml
install -pm 644 config/strangle.yml \
    %{buildroot}%{_datadir}/doc/%{pkgname}/examples/strangle.yml.example
install -pm 644 demo/strangle.yml demo/playbook.yml demo/inventory.ini \
    %{buildroot}%{_datadir}/doc/%{pkgname}/examples/demo/

%pre
if ! getent passwd strangle > /dev/null; then
    useradd --system --user-group --home-dir /var/lib/strangle \
        --no-create-home --shell /sbin/nologin strangle
fi

%post
install -d -o strangle -g strangle -m 0750 /var/lib/strangle
%systemd_post strangle-server.service

%preun
%systemd_preun strangle-server.service

%postun
%systemd_postun_with_restart strangle-server.service

%clean
rm -rf %{buildroot}

%files
%license LICENSE
%{_bindir}/strangle
%{_unitdir}/strangle-server.service
%config(noreplace) %{_sysconfdir}/strangle/server.yml
%config(noreplace) %{_sysconfdir}/strangle/collection.yml
%dir /var/lib/strangle
%{_datadir}/doc/%{pkgname}/examples/

%changelog
* Wed Nov 25 2026 @MAINTAINER@ <@MAINTAINER_EMAIL@> @VERSION@-@RELEASE@
- Package @NAME@ @VERSION@ (built from source).
