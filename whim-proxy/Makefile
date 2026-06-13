# Name of the package
NAME = whim-proxy

# Version
VERSION = 0.1.9

# Revision number
RELEASE = 1

# URL of the project
URL = https://github.com/kakwa/whim-proxy

# short summary of what the package provides
SUMMARY = Webhook relay proxy (server and client)

# Long version of the summary
DESCRIPTION = whim-proxy is a lightweight webhook relay system. The server receives webhooks from external services and relays them to subscribed clients via WebSocket reverse-tunnels, enabling local development and testing of webhook integrations.

# License of the upstream project
LICENSE = MIT

# Allow network for Go module download
COWBUILD_BUILD_ADDITIONAL_ARGS = --use-network yes
MOCK_BUILD_ADDITIONAL_ARGS = --enable-network

###############################################################################
# Source: whim-proxy source tarball from GitHub (build from source)
###############################################################################

URL_SRC = $(URL)/archive/refs/tags/$(VERSION).tar.gz

# Including common rules and targets
include buildenv/Makefile.common

$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST $(DIRECTORIES)
	@$(WGS) -u $(URL_SRC) -o $(SOURCE_ARCHIVE) -C $(CACHE_DIR) -m $(MANIFEST_FILE)
