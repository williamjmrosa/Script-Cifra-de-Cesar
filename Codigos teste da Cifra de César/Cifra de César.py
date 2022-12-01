# coding=UTF-8

string="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890é.,!@#$%¨&*()_+{}[]:;/\?ªº°<>èáàíìÈÉÁÀ"
tam = len(string)
digita = input("Texto para cifrar: ")
desloca = int(input("Deslocamento: "))

def deslocamento():
    global desloca
    if tam > desloca:
         
        return tam
    desloca = desloca - tam
    return deslocamento()
    
print(desloca)
deslocamento()
print(desloca)

def cifrar(texto,desloca):
    textoCifrado = ""
    for letra in texto:
        pos = string.find(letra)
        novaPos = pos + desloca
        if novaPos > tam - 1:
            novaPos = novaPos - tam
        textoCifrado += string[novaPos]
    return textoCifrado
    

def decifrar(textoCifrado,desloca):
    textoDecifrado = ""
    for letra in textoCifrado:
        pos = string.find(letra)
        novaPos = pos - desloca
        if novaPos < 0:
            novaPos = novaPos + tam
        textoDecifrado += string[novaPos]
    return textoDecifrado

texto_cifrado = cifrar(digita,desloca)

print(texto_cifrado,'\n')

texto_decifrado = decifrar(texto_cifrado,desloca)

print(texto_decifrado)
