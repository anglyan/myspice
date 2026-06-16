Usage
-----

The main utility in myspice is ``ngextract``, a script that takes ngspice
output and extracts the data generated using ``.print`` statements so that
it can be easily read and processed by other software.

myspice provides the ``ngextract`` command line tool::

   ngextract --help

For instance, to read an output file from ngspice::

   ngextract -i output.txt

To extract the data from an gspice output file::

   ngextract -i output.txt -o output.dat

Or directly piping the output:

   cat output.txt | ngextract -o output.dat

It can also be used as a library::

   from myspice import io

When used as part of the myspice package, the ``ngextract`` module returns
a dictionary of ``numpy`` arrays, which makes integration with
``matplotlib`` straightforward.
