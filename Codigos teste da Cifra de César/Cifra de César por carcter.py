# coding=UTF-8
'''
string="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890é.,!#$%¨&*()_+{}[]:;/\?ªº°<>èáàíìÈÉÁÀ"
'''
string=" !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþ"
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

def cifrar(caracter,desloca):
    
    pos = string.find(caracter)
    if pos == -1: 
        return caracter
    else:
        novaPos = pos + desloca
    if novaPos > tam - 1:
        novaPos = novaPos - tam
    return string[novaPos]

def decifrar(caracter,desloca):
    
    pos = string.find(caracter)
    if pos == -1:
        return caracter
    else:
        novaPos = pos - desloca
    if novaPos < 0:
        novaPos = novaPos + tam
        
    return string[novaPos]

def lerCifra(texto):
    cifra = ""
    for letra in texto:
        cifra += cifrar(letra,desloca)
    return cifra

def lerDecifra(texto):
    cifra = ""
    for letra in texto:
        cifra += decifrar(letra,desloca)
    return cifra

texto_cifrado = lerCifra(digita)

print(texto_cifrado,'\n')

texto_decifrado = lerDecifra(texto_cifrado)

print(texto_decifrado)
