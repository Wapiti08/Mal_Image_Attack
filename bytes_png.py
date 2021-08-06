import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from math import log
from pathlib import Path
import binascii
import re

def convertAndSave(array, image_path):
    if array.shape[1]!=16: #If not hexadecimal
        assert(False)
    b=int((array.shape[0]*16)**(0.5))
    b=2**(int(log(b)/log(2))+1)
    a=int(array.shape[0]*16/b)
    array=array[:a*b//16,:]
    array=np.reshape(array,(a,b))
    im = Image.fromarray(np.uint8(array))
    im.save(image_path.as_posix(), "PNG")
    return im

if __name__ == "__main__":
    image_path = Path(__file__).parent.resolve().joinpath('test.png')
    bytes_file = Path(__file__).parent.resolve().joinpath('test.bytes')
    print("Processing: ", bytes_file)
    with bytes_file.open('r') as f: 
        array=[]
        for line in f:
            split_line=line.split()
            if len(split_line)!=17:
                continue
            print(split_line)
            array.append([int(i,16) if i!='??' else 0 for i in split_line[1:] ])
        plt.imshow(convertAndSave(np.array(array), image_path))
        del array
        f.close()