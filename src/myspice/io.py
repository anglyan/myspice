import numpy as np

def read_std(filename):
    """
    Read a std output file 
    """

    with open(filename, "r") as f:
        lines = f.readlines()
        content = lines[1:-1]
        header = lines[0].strip().split()[1:]
        data = {col:[] for col in header}
        for line in content:
            row = [float(cell) for cell in line.split()[1:]]
            for i, col in enumerate(header):
                data[col].append(row[i])
        return header, {k:np.array(v) for k, v in data.items()}
    
