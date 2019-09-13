def encrypt(text_to_encrypt, encryption_base = 64):
    digits = []
    for i in range(48,48 + encryption_base):
        digits.append(bytes(chr(i),"utf-8").decode("utf-8"))
    text = text_to_encrypt
    textNum = ""
    result = -1
    remainder = -1
    cipher = """"""
    for s in text:
        m = str(ord(s))
        for i in range(7-len(m)):
            m = f"0{m}"
        textNum = f"{textNum}{m}"
    try:
        result = int(textNum)
    except:
        result = 0
    while result != 0:
        remainder = result % len(digits)
        result = result // len(digits)
        cipher = f"{digits[remainder]}{cipher}"
    return cipher

def decrypt(text_to_decrypt, encryption_base = 64):
    digits = []
    for i in range(48,48 + encryption_base):
        digits.append(bytes(chr(i),"utf-8").decode("utf-8"))
    cipher = text_to_decrypt
    num = 0
    power = len(cipher)-1
    text = ""
    for c in cipher:
        num += (digits.index(c) * (len(digits) ** power))
        power -= 1
    for i in range(7 - (len(str(num)) % 7)):
        num = f"0{num}"
    while num != "":
        text = f"{text}{chr(int(float(num[:7])))}"
        num = num[7:]
    return text
