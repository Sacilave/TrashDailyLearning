from PIL import Image
import numpy as np


def ascii_Img(file):
    im = Image.open(file)
    im = im.convert("L")
    
    simpleRate = 0.15
    
    newImgSize = [int(x * simpleRate) for x in im.size]
    im = im.resize(newImgSize)

    im = np.array(im)

    symbols = np.array(list(" .-vM"))

    im = (im - im.min()) / (im.max() - im.min()) * (symbols.size - 1)
    
    ascii = symbols[im.astype(int)]
    lines = "\n".join(("".join(r) for r in ascii))
    print(lines)

ascii_Img("img01.jpg")
