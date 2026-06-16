import argparse
import sys
import numpy as np


def _parse_lines(lines):
    sweeps = {}
    current_header = None

    for line in lines:
        parts = line.split()
        if not parts:
            continue
        if parts[0] == "Index":
            current_header = tuple(parts[1:])
            if current_header not in sweeps:
                sweeps[current_header] = []
        else:
            try:
                int(parts[0])
                if current_header is not None:
                    sweeps[current_header].append([float(x) for x in parts[1:]])
            except (ValueError, IndexError):
                pass

    if not sweeps:
        return [], np.array([])

    headers_list = list(sweeps.keys())
    first_header = headers_list[0]
    data = np.array(sweeps[first_header])
    all_headers = list(first_header)

    for header in headers_list[1:]:
        other = np.array(sweeps[header])
        data = np.hstack([data, other[:, 1:]])
        all_headers.extend(list(header)[1:])

    return all_headers, data


def ngextract_output(filename):
    """
    Parse an ngspice output file (DC sweep or transient) and return (headers, data).

    headers is a list of column names; data is a numpy array of shape
    (n_points, n_cols). Multiple tables in one file are merged into
    a single array, with the shared first column appearing only once.
    """
    with open(filename, "r") as f:
        return _parse_lines(f)


def ngload(filename):
    """
    Parse an ngspice output file and return a dict mapping each column
    name to its data as a numpy array, e.g. data["time"], data["v(2)"].
    """
    headers, data = ngextract_output(filename)
    return {header: data[:, i] for i, header in enumerate(headers)}


def main():
    parser = argparse.ArgumentParser(
        description="Extract ngspice DC sweep output to a numpy-loadtxt-compatible format."
    )
    parser.add_argument(
        "-i", "--input",
        metavar="FILE",
        help="input file (default: stdin)",
    )
    parser.add_argument(
        "-o", "--output",
        metavar="FILE",
        help="output file (default: stdout)",
    )
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r") as f:
            headers, data = _parse_lines(f)
    else:
        headers, data = _parse_lines(sys.stdin)

    if data.size == 0:
        sys.exit("ngextract: no sweep data found in input")

    if args.output:
        with open(args.output, "w") as f:
            np.savetxt(f, data, header=" ".join(headers))
    else:
        np.savetxt(sys.stdout, data, header=" ".join(headers))
