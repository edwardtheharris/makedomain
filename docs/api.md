---
abstract: Sphinx Contrib Make Domain API Reference
authors: >
   Kay-Uwe (Kiwi) Lorenz <kiwi@franka.dyndns.org>,
   Xander Harris <xandertheharris@gmail.com>
copyright: Copyright (c) 2012, Kay-Uwe (Kiwi) Lorenz, ModuleWorks GmbH
title: Sphinx Contribution Make Domain API Reference
---

This document contains API reference generated from the Sphinx Contrib Make
Domain source code.

```{toctree}
apidocs/sphinxcontrib/sphinxcontrib.makedomain
apidocs/sphinxcontrib/sphinxcontrib
```

## Makefile

```{highlight} make
```

```{default-domain} make
```

```{code-block} make
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
   @$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
   @$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
```

```{target} html
Build the documentation in HTML.
```

```{var} SPHINXOPTS
Sphinx options for passing to the builder.
```

```{automakefile} docs/Makefile
```
