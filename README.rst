=========
olinkform
=========

.. image:: https://img.shields.io/pypi/v/olinkform.svg
        :target: https://pypi.python.org/pypi/olinkform

.. image:: https://github.com/Brodinlab/olinkform/workflows/Python%20package/badge.svg?branch=master

.. image:: https://github.com/Brodinlab/olinkform/workflows/Upload%20Python%20Package/badge.svg


.. image:: https://readthedocs.org/projects/olinkform/badge/?version=latest
        :target: https://olinkform.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status



The preprocessing lib for olink data


* Free software: MIT license
* Documentation: https://olinkform.readthedocs.io.


Usage
-----

Parse a data file

.. code:: python

    from olinkform import parse

    result = parse(path, version)
    # version v1 or v2 are supported,
    # which are corresponding to the old and new olink formats, individually

The result is a dict with the following format

.. code::

    {
        "sampleId": {
            "markerId" : {
                "batch": string
                "value": float,
                "LOD": float,
                "MDF": float
            }
        }
    }

Parse a data file to dataframe

.. code:: python

    from olinkform import parse_to_dataframe

    df = parse_to_dataframe(path, version)


The result is a dataframe with columns:

.. code:: python

    ['batch', 'sample_id','marker', 'value', 'LOD', 'MDF']

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
