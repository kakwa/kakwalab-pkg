# Name of the package
NAME = strangle-server

# Version
VERSION = 0.0.0

# Revision number
RELEASE = 1

# URL of the project
URL = https://github.com/kakwa/strangle

# short summary of what the package provides
SUMMARY = Scheduled Ansible playbook runner (HTTP API and web UI)

# Long version of the summary
DESCRIPTION = strangle applies Ansible playbooks on a schedule and reports results through an HTTP API and web UI. Playbooks run inside embedded CPython worker processes; run metadata, per-host recaps and per-task traces are kept in memory or in PostgreSQL.

# License of the upstream project
LICENSE = GPLv3

# Upstream git revision to build (no release tag for 0.0.0 yet)
REVISION = 4e6ac63c12ef52b22b834769dfcc0e54d7b4a438

# Only build on EL 9+, Debian 13+ and Ubuntu 26.04+
SKIP = <:el:9 <:deb:13 <:ubu:26.04

# Allow network for Go module/toolchain and npm downloads
COWBUILD_BUILD_ADDITIONAL_ARGS = --use-network yes
MOCK_BUILD_ADDITIONAL_ARGS = --enable-network

###############################################################################
# Source: strangle source tarball from a git revision
###############################################################################

# Including common rules and targets
include buildenv/Makefile.common

$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST $(DIRECTORIES)
	@$(GS) -u $(URL) -o $(SOURCE_ARCHIVE) -r $(REVISION) -C $(CACHE_DIR) -m $(MANIFEST_FILE)
