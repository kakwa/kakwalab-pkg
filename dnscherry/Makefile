# Name of the package
NAME = dnscherry

# Version (idem)
VERSION = 0.1.4

# release number 
RELEASE = 1

# external url where to recover the sources
URL=https://github.com/kakwa/dnscherry
URL_SRC=$(URL)/archive/$(VERSION).tar.gz

SUMMARY=DNS management web UI

DESCRIPTION=$(SUMMARY)

LICENSE=MIT

###############################################################################
# Rules #
#########

# Including common rules
include buildenv/Makefile.common

$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	$(WGS) -u $(URL_SRC) -o $(SOURCE_ARCHIVE)
