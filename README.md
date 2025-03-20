[![Build Packages Repositories](https://github.com/kakwa/kakwalab-pkg/actions/workflows/repos.yml/badge.svg)](https://github.com/kakwa/kakwalab-pkg/actions/workflows/repos.yml)

# kakwalab-pkg

Collection of packages of my personal projects.

The `.deb`/`.rpm` repositories are available at the following url: https://kakwa.github.io/kakwalab-pkg/

## Ubuntu/Debian

If you are using `Ubuntu`/`Debian`, here how to install the repository:

```shell
# If you are not root
export SUDO=sudo

# Get your OS version
. /etc/os-release

# Add the GPG key
wget -qO - https://kakwa.github.io/kakwalab-pkg/GPG-KEY.pub | \
    gpg --dearmor | ${SUDO} tee /etc/apt/trusted.gpg.d/kakwalab-pkg.gpg

# Add the repository
echo "deb [arch=$(dpkg --print-architecture)] \
https://kakwa.github.io/kakwalab-pkg/deb.${VERSION_CODENAME}.$(dpkg --print-architecture)/ \
${VERSION_CODENAME} main" | ${SUDO} tee /etc/apt/sources.list.d/kakwalab-pkg.list

# update
apt update
```

## RHEL/Rocky/Fedora

If you are using `RHEL`/`Rocky`/`Fedora`, here how to install the repository:

```shell
# If you are not root
export SUDO=sudo

# Get your OS version
. /etc/os-release

# Determine distro prefix (el for RHEL/Rocky, fc for Fedora)
if [[ "$ID" == "fedora" ]]; then
    DISTRO_PREFIX="fc"
else
    DISTRO_PREFIX="el"
fi

# Create the repository file
cat << EOF | ${SUDO} tee -a /etc/dnf/dnf.conf
[kakwalab-pkg]
name=kakwalab-pkg
baseurl=https://kakwa.github.io/kakwalab-pkg/rpm.${DISTRO_PREFIX}\$releasever.\$basearch/\$releasever/\$basearch/
enabled=1
gpgcheck=1
gpgkey=https://kakwa.github.io/kakwalab-pkg/GPG-KEY.pub
EOF
```

# Building

Check the [pakste documention](https://kakwa.github.io/pakste/).
