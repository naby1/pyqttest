def base64decode(text1: str, text2=""):
    if text2 != "":
        text2 = text2.split('\n')
        for i in text2:
            x = i.strip()
            if len(x) == 64:
                text2 = x
                break
    if len(text2) != 64:
        text2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    text1 = text1.split('\n')
    text1_bin = []
    for i in text1:
        x = i.strip()
        tb = ""
        for j in x:
            if j == '=':
                break
            tb = tb + format(text2.index(j), "06b")
        text1_bin.append(tb)
    res = ""
    for i in text1_bin:
        for j in range(0, len(i), 8):
            a = int(i[j:j + 8], 2)
            res = res + chr(a)
    return res


def bindecode(text):
    res = "八位二进制："
    for i in range(0, len(text), 8):
        res = res + chr(int(text[i:i + 8], 2))
    res = res + '\n'

    res = res + "七位二进制："
    for i in range(0, len(text), 7):
        res = res + chr(int(text[i:i + 7], 2))
    res = res + '\n'

    text1 = ""
    for i in text:
        if i == '0':
            text1 = text1 + '1'
        elif i == '1':
            text1 = text1 + '0'
    res = res + "0和1互换，八位二进制："
    for i in range(0, len(text), 8):
        res = res + chr(int(text1[i:i + 8], 2))
    res = res + '\n'

    res = res + "0和1互换，七位二进制："
    for i in range(0, len(text), 7):
        res = res + chr(int(text1[i:i + 7], 2))
    res = res + '\n'

    return res


def frequencycount(text):
    text_dict = dict()
    for i in text:
        if not text_dict.get(i):
            text_dict[i] = 1
        else:
            text_dict[i] = text_dict[i] + 1
    text_dict = sorted(text_dict.items(), key=lambda x: x[1], reverse=True)
    res = ""
    for i in text_dict:
        res = res + i[0]
    return res
