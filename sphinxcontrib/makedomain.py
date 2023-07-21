# -*- coding: utf-8 -*-
"""A GNU Make domain for Sphinx.

```{rubric} makedomain
```

This domain provides `make:target`, `make:var` and `make:expvar`
directives and roles.

:copyright: 2012 by Kay-Uwe (Kiwi) Lorenz, ModuleWorks GmbH
:license: BSD, see LICENSE for details.
"""

import pathlib
from loguru import logger
from sphinx.util import logging
from sphinxcontrib.domaintools import custom_domain

logger.add(logging.MemoryHandler())
vfile_path = pathlib.Path(f'{pathlib.Path(__file__).parent.parent}/version')
logger.info(f'{vfile_path}')
with vfile_path.open('r', encoding='utf-8') as v_fh:
    __version__ = v_fh.read()

# for this module's sphinx doc
release = __version__
version = release.rsplit('.', 1)[0]


def setup(app):
    """Set up the Make domain extension."""
    app.add_domain(
        custom_domain(
            'GnuMakeDomain',
            name='make',
            label="GNU Make",
            elements={
                'target': {
                    'objname': 'Make Target',
                    'indextemplate': 'pair: %s; Make Target'
                },
                'var': {
                    'objname': 'Make Variable',
                    'indextemplate': 'pair: %s; Make Variable',
                },
                'expvar': {
                    'objname': "Make Variable, exported",
                    'indextemplate': "pair: %s; Make Variable, exported",
                },
            }
        )
    )

# vim: ts=4 : sw=4 : et
