Usage
=====

The main utility in myspice is ``ngextract``, a script that takes ngspice
output and extracts the data generated using ``.print`` statements so that
it can be easily read and processed by other software.

myspice provides the ``ngextract`` command line tool::

   ngextract --help

It can also be used as a library::

   from myspice import io

When used as part of the myspice package, the ``ngextract`` module returns
a dictionary of ``numpy`` arrays, which makes integration with
``matplotlib`` straightforward.
