%define pkgname @NAME@

%global debug_package %{nil}

Name:      %{pkgname}
Version:   @VERSION@
Release:   @RELEASE@%{?dist}
Source:    %{pkgname}-%{version}.tar.gz

URL:       @URL@
Vendor:    @MAINTAINER@
License:   @LICENSE@
Group:     Development/Tools
Summary:   @SUMMARY@
BuildRoot: %{_tmppath}/%{pkgname}-%{_build_arch}-%{version}-%{release}-build

BuildRequires: golang >= 1.21
BuildRequires: git
Requires:      git

%description
@DESCRIPTION@

This package provides the kaclaig CLI and its man page.

%prep
%setup -q -n %{pkgname}-%{version}

%build
export GOPROXY=https://proxy.golang.org
export GOSUMDB=sum.golang.org
export GO111MODULE=on
export CGO_ENABLED=0
export GOTOOLCHAIN=auto
export HOME=%{_builddir}

go build -ldflags="-s -w -X main.version=v%{version}" -o kaclaig ./cmd/kaclaig

%check
export GOPROXY=https://proxy.golang.org
export GOSUMDB=sum.golang.org
export GO111MODULE=on
export GOTOOLCHAIN=auto
export HOME=%{_builddir}

go test ./...

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

install -m 755 kaclaig %{buildroot}%{_bindir}/kaclaig
install -p -m 644 man/kaclaig.1 %{buildroot}%{_mandir}/man1/kaclaig.1

%clean
rm -rf %{buildroot}

%files
%{_bindir}/kaclaig
%{_mandir}/man1/kaclaig.1*

%changelog
* Wed Nov 25 2026 @MAINTAINER@ <@MAINTAINER_EMAIL@> 0.3.0-1
- Package kaclaig 0.3.0 (built from source).
