# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite uma frase: ').upper().strip()

print(f'''
A letra "A" aparecece {frase.count("A")} na frase,
A primeira letra "A" aparece na posição {frase.find("A")+1}
A ultima letra "A" aparece na posição {frase.rfind("A")+1}
''')
