defaultAlphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"," ","%",",","!",".","?","=","*","/","$","@","[","]","{","}","#","&","+","-","\'","\"","°",";"]
digits = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet = defaultAlphabet

def setCustomAlphabet(alpha):
    global alphabet
    print(alpha != [] and alpha != "" and alpha != " " and alpha != [""] and alpha != [" "])
    if alpha != [] and alpha != "" and alpha != " " and alpha != [""] and alpha != [" "]:
        alphabet = alpha
    else:
        alphabet = defaultAlphabet
    print(alpha)
    print(alphabet)

def encrypt(texto):
  text = texto.lower()
  textNum = ""
  result = -1
  remainder = -1
  cipher = """"""
  err = ""
  for s in text:
    if s in alphabet:
      index = alphabet.index(s)+1
      if index < 10:
        index = f"0{index}"
      else:
        index = str(index)
      textNum = f"{textNum}{index}"
    else:
      if err == "":
          err = f"{s}"
      else:
          err = f"{err},{s}"
  #print(textNum)
  try:
      result = int(textNum)
  except:
      result = 0
  #print(result)
  while result != 0:
    remainder = result % 26
    #print(remainder)
    result = result // 26
    #print(result)
    cipher = f"{digits[remainder]}{cipher}"
    #print(cipher)

  if err == "":
      return cipher
  else:
      return f"An error ocured {err} are not in alphabet."

def decrypt(sifra):
  text = ""
  textNum = 0
  cipher = sifra
  power = len(cipher) - 1
  for n in cipher:
    #print(f"textNum = {textNum}, alphabet.index(n) = {alphabet.index(n)}, alphabet.index(n) * (26 ** power) = {alphabet.index(n) * (26 ** power)}, power = {power}")
    textNum += (digits.index(n) * (26 ** power))
    power -= 1
  #print(textNum)
  #textNum = str(textNum)
  if len(str(textNum))/2 != len(str(textNum))//2:
    ind = 1
    text = f"{text}{alphabet[int(str(textNum)[0])-1]}"
    while ind < len(str(textNum)):
      text = f"{text}{alphabet[int(str(textNum)[ind])*10+int(str(textNum)[ind+1])-1]}"
      ind += 2
  else:
    ind = 0
    while ind < len(str(textNum)):
      #print(int(str(textNum)[ind])*10+int(str(textNum)[ind+1]))
      text = f"{text}{alphabet[int(str(textNum)[ind])*10+int(str(textNum)[ind+1])-1]}"
      ind += 2
  return text
