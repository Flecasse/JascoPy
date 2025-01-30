import olefile
import struct
import numpy as np


def jascoData(file_path):
    ole = olefile.OleFileIO(file_path)

    with ole.openstream("DataInfo") as stream:
        data = stream.read()

    *_, n_point, start, end, step = struct.unpack('<LLLLLLddd', data[0:48])
    sigma = np.arange(0, n_point)*step + start

    with ole.openstream("Y-Data") as stream:
        data = stream.read()
        
    y_values = np.frombuffer(data, dtype=np.float32)
    return sigma, y_values