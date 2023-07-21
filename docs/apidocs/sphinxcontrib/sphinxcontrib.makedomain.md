# {py:mod}`sphinxcontrib.makedomain`

```{py:module} sphinxcontrib.makedomain
```

```{autodoc2-docstring} sphinxcontrib.makedomain
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ExpVarDirective <sphinxcontrib.makedomain.ExpVarDirective>`
  - ```{autodoc2-docstring} sphinxcontrib.makedomain.ExpVarDirective
    :summary:
    ```
* - {py:obj}`TargetDirective <sphinxcontrib.makedomain.TargetDirective>`
  - ```{autodoc2-docstring} sphinxcontrib.makedomain.TargetDirective
    :summary:
    ```
* - {py:obj}`VarDirective <sphinxcontrib.makedomain.VarDirective>`
  - ```{autodoc2-docstring} sphinxcontrib.makedomain.VarDirective
    :summary:
    ```
* - {py:obj}`TargetIndex <sphinxcontrib.makedomain.TargetIndex>`
  - ```{autodoc2-docstring} sphinxcontrib.makedomain.TargetIndex
    :summary:
    ```
* - {py:obj}`MakefileDomain <sphinxcontrib.makedomain.MakefileDomain>`
  - ```{autodoc2-docstring} sphinxcontrib.makedomain.MakefileDomain
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`setup <sphinxcontrib.makedomain.setup>`
  - ```{autodoc2-docstring} sphinxcontrib.makedomain.setup
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`vfile_path <sphinxcontrib.makedomain.vfile_path>`
  - ```{autodoc2-docstring} sphinxcontrib.makedomain.vfile_path
    :summary:
    ```
* - {py:obj}`release <sphinxcontrib.makedomain.release>`
  - ```{autodoc2-docstring} sphinxcontrib.makedomain.release
    :summary:
    ```
* - {py:obj}`version <sphinxcontrib.makedomain.version>`
  - ```{autodoc2-docstring} sphinxcontrib.makedomain.version
    :summary:
    ```
````

### API

````{py:data} vfile_path
:canonical: sphinxcontrib.makedomain.vfile_path
:value: >
   None

```{autodoc2-docstring} sphinxcontrib.makedomain.vfile_path
```

````

````{py:data} release
:canonical: sphinxcontrib.makedomain.release
:value: >
   None

```{autodoc2-docstring} sphinxcontrib.makedomain.release
```

````

````{py:data} version
:canonical: sphinxcontrib.makedomain.version
:value: >
   None

```{autodoc2-docstring} sphinxcontrib.makedomain.version
```

````

`````{py:class} ExpVarDirective(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)
:canonical: sphinxcontrib.makedomain.ExpVarDirective

Bases: {py:obj}`sphinx.directives.ObjectDescription`

```{autodoc2-docstring} sphinxcontrib.makedomain.ExpVarDirective
```

```{rubric} Initialization
```

```{autodoc2-docstring} sphinxcontrib.makedomain.ExpVarDirective.__init__
```

````{py:attribute} has_content
:canonical: sphinxcontrib.makedomain.ExpVarDirective.has_content
:value: >
   True

```{autodoc2-docstring} sphinxcontrib.makedomain.ExpVarDirective.has_content
```

````

````{py:attribute} required_arguments
:canonical: sphinxcontrib.makedomain.ExpVarDirective.required_arguments
:value: >
   1

```{autodoc2-docstring} sphinxcontrib.makedomain.ExpVarDirective.required_arguments
```

````

````{py:attribute} option_spec
:canonical: sphinxcontrib.makedomain.ExpVarDirective.option_spec
:value: >
   None

```{autodoc2-docstring} sphinxcontrib.makedomain.ExpVarDirective.option_spec
```

````

````{py:method} handle_signature(sig, signode)
:canonical: sphinxcontrib.makedomain.ExpVarDirective.handle_signature

```{autodoc2-docstring} sphinxcontrib.makedomain.ExpVarDirective.handle_signature
```

````

````{py:method} add_target_and_index(name_cls, sig, signode)
:canonical: sphinxcontrib.makedomain.ExpVarDirective.add_target_and_index

```{autodoc2-docstring} sphinxcontrib.makedomain.ExpVarDirective.add_target_and_index
```

````

`````

`````{py:class} TargetDirective(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)
:canonical: sphinxcontrib.makedomain.TargetDirective

Bases: {py:obj}`sphinx.directives.ObjectDescription`

```{autodoc2-docstring} sphinxcontrib.makedomain.TargetDirective
```

```{rubric} Initialization
```

```{autodoc2-docstring} sphinxcontrib.makedomain.TargetDirective.__init__
```

````{py:attribute} has_content
:canonical: sphinxcontrib.makedomain.TargetDirective.has_content
:value: >
   True

```{autodoc2-docstring} sphinxcontrib.makedomain.TargetDirective.has_content
```

````

````{py:attribute} required_arguments
:canonical: sphinxcontrib.makedomain.TargetDirective.required_arguments
:value: >
   1

```{autodoc2-docstring} sphinxcontrib.makedomain.TargetDirective.required_arguments
```

````

````{py:attribute} option_spec
:canonical: sphinxcontrib.makedomain.TargetDirective.option_spec
:value: >
   None

```{autodoc2-docstring} sphinxcontrib.makedomain.TargetDirective.option_spec
```

````

````{py:method} handle_signature(sig, signode)
:canonical: sphinxcontrib.makedomain.TargetDirective.handle_signature

```{autodoc2-docstring} sphinxcontrib.makedomain.TargetDirective.handle_signature
```

````

````{py:method} add_target_and_index(name_cls, sig, signode)
:canonical: sphinxcontrib.makedomain.TargetDirective.add_target_and_index

```{autodoc2-docstring} sphinxcontrib.makedomain.TargetDirective.add_target_and_index
```

````

`````

`````{py:class} VarDirective(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)
:canonical: sphinxcontrib.makedomain.VarDirective

Bases: {py:obj}`sphinx.directives.ObjectDescription`

```{autodoc2-docstring} sphinxcontrib.makedomain.VarDirective
```

```{rubric} Initialization
```

```{autodoc2-docstring} sphinxcontrib.makedomain.VarDirective.__init__
```

````{py:attribute} has_content
:canonical: sphinxcontrib.makedomain.VarDirective.has_content
:value: >
   True

```{autodoc2-docstring} sphinxcontrib.makedomain.VarDirective.has_content
```

````

````{py:attribute} required_arguments
:canonical: sphinxcontrib.makedomain.VarDirective.required_arguments
:value: >
   1

```{autodoc2-docstring} sphinxcontrib.makedomain.VarDirective.required_arguments
```

````

````{py:attribute} option_spec
:canonical: sphinxcontrib.makedomain.VarDirective.option_spec
:value: >
   None

```{autodoc2-docstring} sphinxcontrib.makedomain.VarDirective.option_spec
```

````

````{py:method} handle_signature(sig, signode)
:canonical: sphinxcontrib.makedomain.VarDirective.handle_signature

```{autodoc2-docstring} sphinxcontrib.makedomain.VarDirective.handle_signature
```

````

````{py:method} add_target_and_index(name_cls, sig, signode)
:canonical: sphinxcontrib.makedomain.VarDirective.add_target_and_index

```{autodoc2-docstring} sphinxcontrib.makedomain.VarDirective.add_target_and_index
```

````

`````

`````{py:class} TargetIndex(domain: sphinx.domains.Domain)
:canonical: sphinxcontrib.makedomain.TargetIndex

Bases: {py:obj}`sphinx.domains.Index`

```{autodoc2-docstring} sphinxcontrib.makedomain.TargetIndex
```

```{rubric} Initialization
```

```{autodoc2-docstring} sphinxcontrib.makedomain.TargetIndex.__init__
```

````{py:attribute} name
:canonical: sphinxcontrib.makedomain.TargetIndex.name
:value: >
   'target'

```{autodoc2-docstring} sphinxcontrib.makedomain.TargetIndex.name
```

````

````{py:attribute} localname
:canonical: sphinxcontrib.makedomain.TargetIndex.localname
:value: >
   'Target Index'

```{autodoc2-docstring} sphinxcontrib.makedomain.TargetIndex.localname
```

````

````{py:attribute} shortname
:canonical: sphinxcontrib.makedomain.TargetIndex.shortname
:value: >
   'Target'

```{autodoc2-docstring} sphinxcontrib.makedomain.TargetIndex.shortname
```

````

````{py:method} generate(docnames=None)
:canonical: sphinxcontrib.makedomain.TargetIndex.generate

```{autodoc2-docstring} sphinxcontrib.makedomain.TargetIndex.generate
```

````

`````

`````{py:class} MakefileDomain(env: sphinx.environment.BuildEnvironment)
:canonical: sphinxcontrib.makedomain.MakefileDomain

Bases: {py:obj}`sphinx.domains.Domain`

```{autodoc2-docstring} sphinxcontrib.makedomain.MakefileDomain
```

```{rubric} Initialization
```

```{autodoc2-docstring} sphinxcontrib.makedomain.MakefileDomain.__init__
```

````{py:attribute} name
:canonical: sphinxcontrib.makedomain.MakefileDomain.name
:value: >
   'make'

```{autodoc2-docstring} sphinxcontrib.makedomain.MakefileDomain.name
```

````

````{py:attribute} roles
:canonical: sphinxcontrib.makedomain.MakefileDomain.roles
:value: >
   None

```{autodoc2-docstring} sphinxcontrib.makedomain.MakefileDomain.roles
```

````

````{py:attribute} directives
:canonical: sphinxcontrib.makedomain.MakefileDomain.directives
:value: >
   None

```{autodoc2-docstring} sphinxcontrib.makedomain.MakefileDomain.directives
```

````

````{py:attribute} indices
:canonical: sphinxcontrib.makedomain.MakefileDomain.indices
:value: >
   None

```{autodoc2-docstring} sphinxcontrib.makedomain.MakefileDomain.indices
```

````

````{py:attribute} initial_data
:canonical: sphinxcontrib.makedomain.MakefileDomain.initial_data
:value: >
   None

```{autodoc2-docstring} sphinxcontrib.makedomain.MakefileDomain.initial_data
```

````

````{py:method} get_full_qualified_name(node)
:canonical: sphinxcontrib.makedomain.MakefileDomain.get_full_qualified_name

```{autodoc2-docstring} sphinxcontrib.makedomain.MakefileDomain.get_full_qualified_name
```

````

````{py:method} get_objects()
:canonical: sphinxcontrib.makedomain.MakefileDomain.get_objects

```{autodoc2-docstring} sphinxcontrib.makedomain.MakefileDomain.get_objects
```

````

````{py:method} resolve_xref(env, fromdocname, builder, typ, target, node, contnode)
:canonical: sphinxcontrib.makedomain.MakefileDomain.resolve_xref

```{autodoc2-docstring} sphinxcontrib.makedomain.MakefileDomain.resolve_xref
```

````

````{py:method} add_expvar(signature, description)
:canonical: sphinxcontrib.makedomain.MakefileDomain.add_expvar

```{autodoc2-docstring} sphinxcontrib.makedomain.MakefileDomain.add_expvar
```

````

````{py:method} add_target(signature, description)
:canonical: sphinxcontrib.makedomain.MakefileDomain.add_target

```{autodoc2-docstring} sphinxcontrib.makedomain.MakefileDomain.add_target
```

````

````{py:method} add_var(signature, description)
:canonical: sphinxcontrib.makedomain.MakefileDomain.add_var

```{autodoc2-docstring} sphinxcontrib.makedomain.MakefileDomain.add_var
```

````

`````

````{py:function} setup(app)
:canonical: sphinxcontrib.makedomain.setup

```{autodoc2-docstring} sphinxcontrib.makedomain.setup
```
````
