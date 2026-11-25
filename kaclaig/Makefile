# Name of the package
NAME = kaclaig

# Version
VERSION = 0.3.0

# Revision number
RELEASE = 1

# URL of the project
URL = https://github.com/kakwa/kaclaig

# short summary of what the package provides
SUMMARY = Keep a Changelog generator from git history using an LLM

# Long version of the summary
DESCRIPTION = kaclaig generates Keep a Changelog-compliant CHANGELOG.md entries from git history using any OpenAI-compatible LLM API. It can print new entries, write them to the changelog, or create dated releases with optional semver conformance checks.

# License of the upstream project
LICENSE = MIT

# go.mod requires Go 1.26; older distributions without GOTOOLCHAIN support
# cannot bootstrap the toolchain from the network.
SKIP = <=:deb:12 <=:ubu:22.04

# Allow network for Go module and toolchain downloads
COWBUILD_BUILD_ADDITIONAL_ARGS = --use-network yes
MOCK_BUILD_ADDITIONAL_ARGS = --enable-network

###############################################################################
# Source: kaclaig source tarball from GitHub (build from source)
###############################################################################

URL_SRC = $(URL)/archive/refs/tags/$(VERSION).tar.gz

# Including common rules and targets
include buildenv/Makefile.common

$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST $(DIRECTORIES)
	@$(WGS) -u $(URL_SRC) -o $(SOURCE_ARCHIVE) -C $(CACHE_DIR) -m $(MANIFEST_FILE)
