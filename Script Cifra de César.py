# -*- coding: utf-8 -*-
import sys
import os

# Diferencial foi implementado espaço e caracteres especiais e acentuação e numeros
caracteres = " ! \"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþ"

#Diferencial calcula o deslocamento pela senha
def deslocamento():
	global senha
	
	if type(senha) == str:
		numero = 0
		for valor in senha:
			numero += ord(valor)
		senha = numero
		
	if tamanho < senha:
		senha = senha - tamanho
		return deslocamento()
	
#cifra o caracter do texto
def cifrar(caracter,desloca):
    
    pos = caracteres.find(caracter)
    if pos == -1: 
        return caracter
    else:
        novaPos = pos + desloca
    if novaPos > tamanho - 1:
        novaPos = novaPos - tamanho
    return caracteres[novaPos]
	
#decifra o caracter do texto
def decifrar(caracter,desloca):
    
    pos = caracteres.find(caracter)
    if pos == -1:
        return caracter
    else:
        novaPos = pos - desloca
    if novaPos < 0:
        novaPos = novaPos + tamanho 
    return caracteres[novaPos]

#cria arquivo
def criarArquivo(nome,texto_cifrado):
	novoArquivo = open(nome,"w")

	novoArquivo.write(texto_cifrado)
	novoArquivo.close()
#lê o texto para cifrar e decifrar
def ler():
	try:
		deslocamento()
		
		cifra = ""
		arquivo = open(localArquivo,"r") 
		nomeArquivo = localArquivo.split("-")
		nomeArquivo = nomeArquivo[len(nomeArquivo) - 1]
		if tipo == "cifrar":	
			for letra in arquivo.read():
				cifra += cifrar(letra,senha)
			
			criarArquivo("cifrar-"+nomeArquivo,cifra)
			
		elif tipo == "decifrar":
			for letra in arquivo.read():
				cifra += decifrar(letra,senha)
			criarArquivo("decifrar-"+nomeArquivo,cifra)
		else:
			print("Entra do que fazer errada")
		arquivo.close()
	except FileNotFoundError:
		print("Arquivo não existe")
	
if len(sys.argv) == 4:
	tamanho = len(caracteres)
	localArquivo = sys.argv[1];
	senha = sys.argv[2];
	tipo = sys.argv[3];

	texto_cifrado = ler()
else:
	print("Falta informações de entrada")