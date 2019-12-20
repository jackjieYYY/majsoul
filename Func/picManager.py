from PIL import Image
import json
from aip import AipOcr

APP_ID = '18049881'
API_KEY = 'hRktOQKZQcyc3oVLsTEtiUmY'
SECRET_KEY = 'P7DgdBrEvj4AazB2RpdxznSdtYbozmSa'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def checkColor(image_path,data):
    '''
    :param image_path: a str, exp: /xxx/2019-08-14_17-26-01.png
    :param data: dic, exp: {(100,100):"#3BC9FFFF"}

    :return True or False
    '''
    img_src = Image.open(image_path)
    img_src = img_src.convert('RGB')
    str_strlist = img_src.load()
    for key,value in data.items():
        colorRGBA = str_strlist[key[0],key[1]]
        if value != RGBA_to_Hex(colorRGBA):
            img_src.close()
            return False
    
    img_src.close()
    return True

def checkColor_Block(image_path,data):
    '''
    :param image_path: a str, exp: /xxx/2019-08-14_17-26-01.png
    :param data: dic, exp: {(100,100):"#3BC9FFFF"}

    :return True or False
    '''
    img_src = Image.open(image_path)
    img_src = img_src.convert('RGB')
    str_strlist = img_src.load()

    

    colorA=data[0]
    colorB=data[1]

    X=colorA[0]
    Y=colorA[1]
    firstColor= str_strlist[X,Y]
    while Y<=colorB[1]:
        while X<=colorB[0]:
            colorRGBA = str_strlist[X,Y]
            if colorRGBA != firstColor:
                return False
            X=X+1
        Y=Y+1
    img_src.close()
    return True

def getCoin():
    img = Image.open("screenshot.png")
    img2 = img.crop((670, 230, 750, 260))
    img2.save("coin.png")
    image = get_file_content('coin.png')
    text = client.basicGeneral(image)
    data=json.loads(json.dumps(text))
    return data['words_result'][0]['words']

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()



def RGBA_to_Hex(RGBA):
    '''
    :param RGBA: a tuple, exp: (59, 201, 255, 255)
    :return hex_str: a str, exp: #3BC9FFFF
    '''
    
    hex_str = '#'
    for i in RGBA:
        num = int(i) # 将RGBA的数值转换成数字类型
        hex_str = hex_str + str(hex(num))[2:].replace('x', '0').upper()
    return hex_str






