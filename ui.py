import PySimpleGUI as sg
from coder import encrypt, decrypt

layout = [[sg.Text("Encode:")],
          [sg.InputText(), sg.Button("Encode")],
          [sg.Text("Decode:")],
          [sg.InputText(), sg.Button("Decode")],
          [sg.Text("Base"), sg.InputText(size=(5, None), default_text="64")],
          [sg.Output()]]

window = sg.Window("Encryptor App", layout, resizable=True)
while True:
    event, values = window.read()
    try:
        if event == None:
            break
        if event == "Encode":
            print(encrypt(values[0],encryption_base=int(values[2])))
        if event == "Decode":
            print(decrypt(values[1],encryption_base=int(values[2])))
    except Exception as e:
        print(e)
window.close()
