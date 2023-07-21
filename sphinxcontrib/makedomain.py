# -*- coding: utf-8 -*-
"""A GNU Make domain for Sphinx.

```{rubric} makedomain
```

This domain provides `make:target`, `make:var` and `make:expvar`
directives and roles.

:copyright: 2012 by Kay-Uwe (Kiwi) Lorenz, ModuleWorks GmbH
:license: BSD, see LICENSE for details.
:var version: Current version minus the last dot
"""

import pathlib

from collections import defaultdict

from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive
from loguru import logger
from sphinx import addnodes
from sphinx.directives import ObjectDescription
from sphinx.domains import Domain
from sphinx.domains import Index
from sphinx.roles import XRefRole
from sphinx.util import logging
from sphinx.util.nodes import make_refnode

logger.add(logging.MemoryHandler())
vfile_path = pathlib.Path(f'{pathlib.Path(__file__).parent.parent}/version')
logger.info(f'{vfile_path}')
with vfile_path.open('r', encoding='utf-8') as v_fh:
    __version__ = v_fh.read()

#: for this module's sphinx doc
release = __version__
#: Current version minus the last dot
version = release.rsplit('.', 1)[0]


class ExpVarDirective(ObjectDescription):
    """A custom directive that describes a make exported variable."""

    has_content = True
    required_arguments = 1
    option_spec = {
        'description': directives.unchanged_required,
    }

    def handle_signature(self, sig, signode):
        """Handle exported variable signatures."""
        signode += addnodes.desc_name(text=sig)
        return sig

    def add_target_and_index(self, name_cls, sig, signode):
        """Add reference target and index."""
        signode['ids'].append('target' + '-' + sig)
        if 'description' in self.options:
            description = [
                x.strip() for x in self.options.get('description').split(',')]

            targets = self.env.get_domain('expvar')
            targets.add_target(sig, description)


class TargetDirective(ObjectDescription):
    """A custom directive that describes a make target."""

    has_content = True
    required_arguments = 1
    option_spec = {
        'description': directives.unchanged_required,
    }

    def handle_signature(self, sig, signode):
        """Handle target signatures."""
        signode += addnodes.desc_name(text=sig)
        return sig

    def add_target_and_index(self, name_cls, sig, signode):
        """Add reference target and index."""
        signode['ids'].append('target' + '-' + sig)
        if 'description' in self.options:
            description = [
                x.strip() for x in self.options.get('description').split(',')]

            targets = self.env.get_domain('target')
            targets.add_target(sig, description)


class VarDirective(ObjectDescription):
    """A custom directive that describes a make variable."""

    has_content = True
    required_arguments = 1
    option_spec = {
        'description': directives.unchanged_required,
    }

    def handle_signature(self, sig, signode):
        """Handle exported variable signatures."""
        signode += addnodes.desc_name(text=sig)
        return sig

    def add_target_and_index(self, name_cls, sig, signode):
        """Add reference target and index."""
        signode['ids'].append('target' + '-' + sig)
        if 'description' in self.options:
            description = [
                x.strip() for x in self.options.get('description').split(',')]

            targets = self.env.get_domain('var')
            targets.add_target(sig, description)


class TargetIndex(Index):
    """A custom index that creates an recipe matrix."""

    name = 'target'
    localname = 'Target Index'
    shortname = 'Target'

    def generate(self, docnames=None):
        """Generate an index of Make targets."""
        content = defaultdict(list)

        # sort the list of recipes in alphabetical order
        recipes = self.domain.get_objects()
        recipes = sorted(recipes, key=lambda recipe: recipe[0])

        # generate the expected output, shown below, from the above using the
        # first letter of the recipe as a key to group things
        #
        # name, subtype, docname, anchor, extra, qualifier, description
        for _name, dispname, typ, docname, anchor, _priority in recipes:
            content[dispname[0].lower()].append(
                (dispname, 0, docname, anchor, docname, '', typ))

        # convert the dict to the sorted list of tuples expected
        content = sorted(content.items())

        return content, True


class MakefileDomain(Domain):
    """Define methods and attributes of the Makefile Domain."""

    name = 'make'
    roles = {
        'expvar': XRefRole(),
        'target': XRefRole(),
        'var': XRefRole(),
    }
    directives = {
        'expvar': ExpVarDirective,
        'target': TargetDirective,
        'var': VarDirective,
    }
    indices = {
        TargetIndex,
    }
    initial_data = {
        'targets': [],  # object list
        'expvars': {},
        'vars': {},  # name -> object
    }

    def get_full_qualified_name(self, node):
        """Return a qualified target name."""
        return f'target.{node.arguments[0]}'

    def get_objects(self):
        """Return the list of targets."""
        yield from self.data['targets']

    def resolve_xref(self, env, fromdocname, builder, typ, target, node,
                     contnode):
        """Resolve any cross references."""
        match = [(docname, anchor)
                 for name, sig, typ, docname, anchor, prio
                 in self.get_objects() if sig == target]

        if len(match) > 0:
            todocname = match[0][0]
            targ = match[0][1]

            return make_refnode(builder, fromdocname, todocname, targ,
                                contnode, targ)
        else:
            logger.info('Awww, found nothing')
            return None

    def add_expvar(self, signature, description):
        """Add a new exported variable to the domain."""
        name = f'expvar.{signature}'
        anchor = f'expvar-{signature}'

        self.data['expvar'][name] = description
        # name, dispname, type, docname, anchor, priority
        self.data['expvars'].append(
            (
                name, signature, 'Exported Variable',
                self.env.docname, anchor, 0
            )
        )

    def add_target(self, signature, description):
        """Add a new target to the domain."""
        name = f'target.{signature}'
        anchor = f'target-{signature}'

        self.data['target'][name] = description
        # name, dispname, type, docname, anchor, priority
        self.data['targets'].append(
            (name, signature, 'Target', self.env.docname, anchor, 0))

    def add_var(self, signature, description):
        """Add a new target to the domain."""
        name = f'var.{signature}'
        anchor = f'var-{signature}'

        self.data['var'][name] = description
        # name, dispname, type, docname, anchor, priority
        self.data['var'].append(
            (name, signature, 'Variable', self.env.docname, anchor, 0))


def setup(app):
    """Set up the Make domain extension.

    Previously used the domain tools custom domain package.

    ```{code-block} python
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
    ```
    """
    app.add_domain(MakefileDomain)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

# vim: ts=4 : sw=4 : et
