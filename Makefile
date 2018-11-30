# Minimal makefile for Sphinx documentation

# A "-W" option turns warnings into errors. Good way to prevent errors (like
# misspelled filenames) from creeping in.
SPHINXOPTS    = -W
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = lizard
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%:
	@$(SPHINXBUILD) -b $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
