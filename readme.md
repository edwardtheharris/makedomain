# GNU Make Domain

This [Sphinx extension](http://sphinx-doc.org) provides a
[GNU Make](http://www.gnu.org/software/make/)
[domain](http://sphinx-doc.org/domains.html). These documents are published
to [GitHub Pages](https://edwardtheharris.github.io/makedomain/).

## Installation

```{code-block} shell
pip install sphinxcontrib-makedomain
```

## Enable Extension

Add ``sphinxcontrib.makedomain`` to the `extensions` setting in {file}`conf.py`.

```{code-block} python
extensions = [ 'sphinxcontrib.makedomain' ]
```

## Usage

Get ready for make.

```{code-block} rst
:caption: rST

.. highlight:: make

.. default-domain:: make
```

````{code-block} markdown
:caption: MyST Markdown

```{highlight} make
```

```{default-domain} make
```
````

### Targets

Describe a target

````{code-block} rST
:caption: rST

.. target:: all

   describe here whatever :target:`all` does
````

````{code-block} markdown
:caption: MyST Markdown

```{target} all
describe here whatever {target}`all` does
```
````

### Variables

Describe a variable.

```{code-block} rst
:caption: rST

.. var:: MY_VAR

   Describe here whatever :var:`MY_VAR` does.
```

````{code-block} markdown
:caption: MyST Markdown

```{var} MY_VAR
Describe here whatever {var}`MY_VAR` does.
```
````

Describe an exported variable.

````{code-block} rst
:caption: rST

.. expvar:: EXPORTED_VAR

   Describe here whatever :expvar:`EXPORTED_VAR` does.

   This would describe::

      export EXPORTED_VAR = some string
````

````{code-block} markdown
:caption: MyST Markdown

```{expvar} EXPORTED_VAR
Describe here whatever {expvar}`EXPORTED_VAR` does.

This would describe:

    export EXPORTED_VAR = some string
```
````

## License

[New BSD License](/license.md)

## Author

```{sectionauthor} Kay-Uwe (Kiwi) Lorenz <kiwi@franka.dyndns.org> (http://quelltexter.org)
```
