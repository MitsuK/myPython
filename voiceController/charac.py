# -*- coding: utf-8 -*-
from PIL import Image
import codecs
import json

_image = None

def RGBA2Gray(rgba):
    return int((rgba[0] + rgba[1] + rgba[2]) / 3)

def getChar(cord):
    offsetX = 8 + 0
    offsetY = 12 + 0
    arrays = []
    for y in range(12):
        _arr = []
        for x in range(8):
            #_arr.append("8")
            _arr.append(0)
            #if (RGBA2Gray(img.getpixel((x + 0,y + 70)))) > 128:
            if (RGBA2Gray(img.getpixel((x + cord[0] * offsetX, y + cord[1] * offsetY)))) < 128:
                #_arr[x] = " "
                _arr[x] = 1
        arrays.append(_arr)
        print(_arr)
    return arrays

if __name__ == "__main__":
    img = Image.open("fonts/k8x12_jisx0208.png").convert('RGBA')
    _image = img
    uni = u'ワトソン君こちらへ来てくれないか'
    _cord = [0,0]
    rtn = []
    for i in range(len(uni)):
        dat = codecs.encode(uni[i].encode("euc-jp"), 'hex_codec')
        _cord[1] = (int(dat[0:2], 16) - int("a1", 16))
        _cord[0] = (int(dat[2:4], 16) - int("a1", 16))
        print(uni[i], _cord)
        rtn.append(getChar(_cord))
    f = open("phraseDots.js", "w")
    f.write("_data = " + json.dumps(rtn) + ";")
    f.close()
    #print(type(uni.decode("utf-8")))
    #print int(uni.decode("shift-jis").encode("shift-jis")[0])
    #print(arrays)
