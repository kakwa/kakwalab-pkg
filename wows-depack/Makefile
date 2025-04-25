# Name of the package
NAME = wows-depack

# Version
VERSION = 0.3.0

# Revision number 
RELEASE = 1

# URL of the project 
URL=https://github.com/wows-tools/wows-depack/

# short summary of what the package provides
SUMMARY=World of Warships resource unpack tool & library

# long version of the summary
DESCRIPTION=wows-depack is a tool and library for unpacking World of Warships game resources. It provides both a command-line interface and a C library for programmatic access.

LICENSE=MIT

###############################################################################
# Rule #
########

# example of source recovery url
URL_SRC=$(URL)/archive/$(VERSION).tar.gz

# Including common rules and targets 
include buildenv/Makefile.common

# preparation hook for rpm package
# source archives must recovered here
# and their content put inside $(BUILD_DIR)/src
#
# $(WGS) should be the prefered way to recover archives
# (add checksum against a manifest file).
# use 'make manifest' to generate/update this manifest file.

$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	$(WGS) -u $(URL_SRC) -o $(SOURCE_ARCHIVE)
