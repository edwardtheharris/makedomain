# {py:mod}`sphinxcontrib.automakefile`

```{py:module} sphinxcontrib.automakefile
```

```{autodoc2-docstring} sphinxcontrib.automakefile
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TreeNode <sphinxcontrib.automakefile.TreeNode>`
  - ```{autodoc2-docstring} sphinxcontrib.automakefile.TreeNode
    :summary:
    ```
* - {py:obj}`AutoMakefileDirective <sphinxcontrib.automakefile.AutoMakefileDirective>`
  - ```{autodoc2-docstring} sphinxcontrib.automakefile.AutoMakefileDirective
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`setup <sphinxcontrib.automakefile.setup>`
  - ```{autodoc2-docstring} sphinxcontrib.automakefile.setup
    :summary:
    ```
````

### API

`````{py:class} TreeNode(value, comments, parent=None)
:canonical: sphinxcontrib.automakefile.TreeNode

```{autodoc2-docstring} sphinxcontrib.automakefile.TreeNode
```

```{rubric} Initialization
```

```{autodoc2-docstring} sphinxcontrib.automakefile.TreeNode.__init__
```

````{py:method} add_child(value)
:canonical: sphinxcontrib.automakefile.TreeNode.add_child

```{autodoc2-docstring} sphinxcontrib.automakefile.TreeNode.add_child
```

````

````{py:method} remove_child()
:canonical: sphinxcontrib.automakefile.TreeNode.remove_child

```{autodoc2-docstring} sphinxcontrib.automakefile.TreeNode.remove_child
```

````

`````

`````{py:exception} AutoMakefileException(message: str, orig_exc: Exception | None = None, modname: str | None = None)
:canonical: sphinxcontrib.automakefile.AutoMakefileException

Bases: {py:obj}`sphinx.errors.ExtensionError`

```{autodoc2-docstring} sphinxcontrib.automakefile.AutoMakefileException
```

```{rubric} Initialization
```

```{autodoc2-docstring} sphinxcontrib.automakefile.AutoMakefileException.__init__
```

````{py:attribute} category
:canonical: sphinxcontrib.automakefile.AutoMakefileException.category
:value: >
   'AutoMakefile error'

```{autodoc2-docstring} sphinxcontrib.automakefile.AutoMakefileException.category
```

````

`````

`````{py:class} AutoMakefileDirective(name, arguments, options, content, lineno, content_offset, block_text, state, state_machine)
:canonical: sphinxcontrib.automakefile.AutoMakefileDirective

Bases: {py:obj}`docutils.parsers.rst.Directive`

```{autodoc2-docstring} sphinxcontrib.automakefile.AutoMakefileDirective
```

```{rubric} Initialization
```

```{autodoc2-docstring} sphinxcontrib.automakefile.AutoMakefileDirective.__init__
```

````{py:attribute} required_arguments
:canonical: sphinxcontrib.automakefile.AutoMakefileDirective.required_arguments
:value: >
   1

```{autodoc2-docstring} sphinxcontrib.automakefile.AutoMakefileDirective.required_arguments
```

````

````{py:method} run()
:canonical: sphinxcontrib.automakefile.AutoMakefileDirective.run

```{autodoc2-docstring} sphinxcontrib.automakefile.AutoMakefileDirective.run
```

````

````{py:method} _get_comments(source, source_file)
:canonical: sphinxcontrib.automakefile.AutoMakefileDirective._get_comments

```{autodoc2-docstring} sphinxcontrib.automakefile.AutoMakefileDirective._get_comments
```

````

````{py:method} _parse_document(doc, comments)
:canonical: sphinxcontrib.automakefile.AutoMakefileDirective._parse_document

```{autodoc2-docstring} sphinxcontrib.automakefile.AutoMakefileDirective._parse_document
```

````

````{py:method} _generate_documentation(tree)
:canonical: sphinxcontrib.automakefile.AutoMakefileDirective._generate_documentation

```{autodoc2-docstring} sphinxcontrib.automakefile.AutoMakefileDirective._generate_documentation
```

````

````{py:method} _parse_file(source_file)
:canonical: sphinxcontrib.automakefile.AutoMakefileDirective._parse_file

```{autodoc2-docstring} sphinxcontrib.automakefile.AutoMakefileDirective._parse_file
```

````

`````

````{py:function} setup(app)
:canonical: sphinxcontrib.automakefile.setup

```{autodoc2-docstring} sphinxcontrib.automakefile.setup
```
````
