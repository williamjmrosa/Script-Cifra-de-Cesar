# -*- coding: utf-8 -*-
'''
string="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890é.,!#$%¨&*()_+{}[]:;/\?ªº°<>èáàíìÈÉÁÀ"
'''
string="!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþ"
tam = len(string)
digita = input("Local do texto para cifrar: ")
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
    padronizar = ""
    cifra = ""
    for letra in texto:
        print(letra)
        padronizar += letra
    texto = padronizar
    for letra in texto:
        cifra += cifrar(letra,desloca)
    return cifra

def lerDecifra(texto):
    cifra = ""
    for letra in texto:
        cifra += decifrar(letra,desloca)
    return cifra

arquivo = open(digita,"r")

texto_cifrado = lerCifra(arquivo)
arquivo.close()

arquivo = open("cifrado-"+digita,"w")

arquivo.write(texto_cifrado)
arquivo.close()


arquivo_texto_decifrado = lerDecifra(texto_cifrado)
print("decifrado")
print(arquivo_texto_decifrado)
arquivo = open("decifra"+digita,"w")
arquivo.write(arquivo_texto_decifrado)
arquivo.close()


