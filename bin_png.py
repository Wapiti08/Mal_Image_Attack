import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from math import log
from pathlib import Path
import binascii
import re

def convertAndSave(array, file_name, image_path):
    print('Processing '+ name)
    # same as the hexdump format, there are 32 bytes data in a row
    if array.shape[1]!=32: #If not hexadecimal
        assert(False)
    b=int((array.shape[0]*32)**(0.5))
    b=2**(int(log(b)/log(2))+1)
    a=int(array.shape[0]*32/b)
    array=array[:a*b//32,:]
    array=np.reshape(array,(a,b))
    im = Image.fromarray(np.uint8(array))
    im.save(image_path.as_posix(), "PNG")
    return im

if __name__ == "__main__":

    name = '8'
    image_path = Path(__file__).parent.resolve().joinpath('8','binary.png')
    hexdata = []
    encoding = 'utf-8'
    with open('./8/binary', 'rb') as f:
        for chunk in iter(lambda: f.read(16), b''):
            print(binascii.hexlify(chunk))
            hexdata.append(binascii.hexlify(chunk).decode(encoding))
        
        array = []
        for line in hexdata:
            hex_data = re.findall(r"\w{2}",line)
            if len(hex_data) !=16:
                continue
            array.append([int(i,16) if i!='??' else 0 for i in line ])
        plt.imshow(convertAndSave(np.array(array), name, image_path))
        del array

