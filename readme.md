# GNU Make Domain

This [Sphinx extension](http://sphinx-doc.org) provides a
[GNU Make](http://www.gnu.org/software/make/)
[domain](http://sphinx-doc.org/domains.html).

## Installation

```{code-block} shell
pip install sphinxcontrib-makedomain
```

## Enable Extension

Add ``sphinxcontrib.makedomain`` to the `extensions` setting in {file}`conf.py`.

```{code-block} python
extensions = [ 'sphinxcontrib.makedomain' ]
```

Usage
-----

Get ready for make::

    .. highlight:: make

    .. default-domain:: make

Describe a target::

    .. target:: all

       describe here whatever :target:`all` does

Describe a variable::

    .. var:: MY_VAR

       Describe here whatever :var:`MY_VAR` does.

Describe an exported variable::

    .. expvar:: EXPORTED_VAR

       Describe here whatever :expvar:`EXPORTED_VAR` does.

       This would describe::

           export EXPORTED_VAR = some string


License
-------

New BSD License.


Author
------

`Kay-Uwe (Kiwi) Lorenz <kiwi@franka.dyndns.org>`_ (http://quelltexter.org)
