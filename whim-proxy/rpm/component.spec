%define pkgname @NAME@
%define _unitdir /usr/lib/systemd/system/

%global debug_package %{nil}

Name:      whim-server
Version:   @VERSION@
Release:   @RELEASE@%{?dist}
Source:    %{pkgname}-%{version}.tar.gz
Source1:   whim-server.service

URL:       @URL@
Vendor:    @MAINTAINER@
License:   MIT
Group:     System/Servers
Summary:   @SUMMARY@ - server
BuildRoot: %{_tmppath}/%{pkgname}-%{_build_arch}-%{version}-%{release}-build

BuildRequires: golang >= 1.21
BuildRequires: systemd-rpm-macros
Requires:      systemd

%description
@DESCRIPTION@

This package provides the whim-server binary and systemd service unit.

%package -n whim-client
Summary: @SUMMARY@ - client
Group:   Applications/Internet

%description -n whim-client
@DESCRIPTION@

This package provides the whim-client binary for local webhook relay.

%prep
%setup -q -n %{pkgname}-%{version}

%build
export GOPROXY=https://proxy.golang.org
export GOSUMDB=sum.golang.org
export GO111MODULE=on
export CGO_ENABLED=0
export GOTOOLCHAIN=auto
export HOME=%{_builddir}

cp logo.svg internal/web/static/favicon.svg
mkdir -p internal/web/clients
for pair in linux/amd64 linux/arm64 darwin/amd64 darwin/arm64 windows/amd64 windows/arm64; do
    os=$(echo $pair | cut -d/ -f1)
    arch=$(echo $pair | cut -d/ -f2)
    ext=""
    if [ "$os" = "windows" ]; then ext=".exe"; fi
    GOOS=$os GOARCH=$arch go build -ldflags="-s -w" \
        -o internal/web/clients/whim-client-$os-$arch$ext ./cmd/client
done
go build -ldflags="-s -w" -o whim-server ./cmd/server
go build -ldflags="-s -w" -o whim-client ./cmd/client

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

install -m 755 whim-server %{buildroot}%{_bindir}/whim-server
install -m 755 whim-client %{buildroot}%{_bindir}/whim-client
install -pm 644 %{SOURCE1} %{buildroot}%{_unitdir}/whim-server.service

%pre
if ! getent passwd whim > /dev/null ; then
    useradd --system --home-dir /var/lib/whim \
        --no-create-home --shell /sbin/nologin whim
fi

%post
%systemd_post whim-server.service

%preun
%systemd_preun whim-server.service

%postun
%systemd_postun_with_restart whim-server.service

%clean
rm -rf %{buildroot}

%files
%{_bindir}/whim-server
%{_unitdir}/whim-server.service

%files -n whim-client
%{_bindir}/whim-client

%changelog
* Sat Jun 13 2026 @MAINTAINER@ <@MAINTAINER_EMAIL@> 0.1.9-1
- Package whim-proxy 0.1.9 (built from source).
