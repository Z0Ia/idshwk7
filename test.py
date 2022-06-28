from PIL import Image
def mod(x, y):
    return x % y

def toasc(strr):
    return int(strr, 2)

def plus(string1):
    return string1.zfill(8)

def get_key(strr):
    string1 = ""
    for i in range(len(strr)):
        string1 = string1 + "" + plus(bin(ord(strr[i])).replace('0b', ''))
    return string1

def encode(str1, str2, str3):
    im = Image.open(str1)
    # 获取图片的宽和高
    width, height = im.size[0], im.size[1]
    key = get_key(str2)
    keylen = len(key)
    count = 0
    for h in range(height):
        for w in range(width):
            pixel = im.getpixel((w, h))
            a = pixel[0]
            b = pixel[1]
            c = pixel[2]
            if count == keylen:
                break
            a = a - mod(a, 2) + int(key[count])
            im.putpixel((w, h), (a, b, c))
            count += 1
        if count == keylen:
            break
    im.save(str3)

def decode(str1, New_Graph):
    b = ""
    im = Image.open(New_Graph)
    lenth = str1 * 8
    width, height = im.size[0], im.size[1]
    count = 0
    for h in range(height):
        for w in range(width):
            pixel = im.getpixel((w, h))
            if count == lenth:
                break
            count += 1
            b = b + str(mod(int(pixel[0]), 2))

        if count == lenth:
            break
    result_str = ""
    for i in range(0, len(b), 8):
        # 以每8位为一组二进制，转换为十进制
        stra = toasc(b[i:i + 8])
        result_str += chr(stra)
    return  result_str

if __name__ == '__main__':
    # 原始图片
    Graph_name = "carrier.png"
    # 嵌入字符串
    Watermark_str = "57119313_zuola"
    # 保存的文件
    To_Graph = "result_with_watermark.png"
    # 提取的字符长度
    Watermark_len = len(Watermark_str)
    # 提取的新信息文件
    New_Graph = "result_with_watermark.png"
    #加密操作
    encode(Graph_name, Watermark_str, To_Graph)
    #解密操作
    new_str=decode(Watermark_len, New_Graph)
    print("Origin str is:",Watermark_str)
    print("Extract str is:",new_str)