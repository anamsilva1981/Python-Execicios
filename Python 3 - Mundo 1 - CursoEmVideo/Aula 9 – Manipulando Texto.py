# Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

## FATIAMENTO ##

frase = "CURSO EM VIDEO PYTHON"

#Imprime a 10 letra da frase "V"
print(frase[9])

#Imprime do 9º ao 12º "VIDE"
print(frase[9:13])

#Imprime do 9º ao 21 "VIDEO PYTHON"
print(frase[9:21])

#Imprime do 9º ao 21 pulando dois numeros "VDOPTO"
print(frase[9:21:2])

#Imprime do 1º caracter até o 5º "CURSO"
print(frase[:5])

#Imprime do 15º caracter até o final "PYTHON"
print(frase[15:])

#Imprime a partir do 9º pulando 3 casas "VEPH"
print(frase[9::3])


### ANÁLISE ###

frase = "CURSO EM VIDEO PYTHON"

#Imprime o comprimento da frase
print(len(frase))

#Imprime na tela a quantidade de letras solicitadas 
print(frase.count('O'))

#Imprime quando começou a informação solicitada
print(frase.find('DEO'))

#Imprime a posição "-1" quando ele não encontra a string que procuramos 
print(frase.find('Android'))

#Retorna V or F para o informação solicitada
print('CURSO' in frase)

print( ' :::::: TRANSFORMAÇÃO :::::: ')

#Altera uma informação pela outra
print(frase.replace('PYTHON','ANDROID'))

#Altera a sentença em maiuscula
print(frase.upper())

#Altera a sentença em minusculo
print(frase.lower())

#Coloca toda a senteça em minuscula exceto a primeira letra
print(frase.capitalize())

#Analisa a qtde de palavras na frase e coloca a primeira letra em maiuscula
print(frase.title())

#Remove espaço no inicio e final da string
print(frase.strip())

#Remove espaço no lado direita da string
print(frase.rstrip())

#Remove espaço no lado esquerdo da string
print(frase.lstrip())
