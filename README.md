# myspice

A collection of utilities to work with SPICE simulations

## Installation

```
pip install myspice
```

## About

`myspice` was created as a tool to help
with the building of [ngspice](https://ngspice.sourceforge.io) tutorials.

Since others may find it useful, I
have released it with a permissive license. My plan is to keep adding
functionality as it matures.

The main utility in `myspice` is `ngextract`, a script that takes ngspice
output and extracts the data generated
using `.print` statements so that it can be easily read and processed by other software. I wanted to have a simple command line tool.

When used as part of the `myspice` package, the `ngextract` module returns
a dictionary of `numpy` arrays, which makes integration with `matplotlib` straightforward.

## What myspice is not

There are other good Python packages that provide a more comprehensive integration with solvers such as ngspice or Xyce:

- [`PySpice`](https://github.com/FabriceSalvaire/PySpice) — Simulates circuits with ngspice or Xyce and builds netlists directly from Python.
- [`PyLTSpice`](https://github.com/nunobrum/PyLTSpice) — Automates running and parsing results from LTspice.
- [`spicelib`](https://github.com/nunobrum/spicelib) — Successor to PyLTSpice, with broader support for LTspice, ngspice, and Xyce.