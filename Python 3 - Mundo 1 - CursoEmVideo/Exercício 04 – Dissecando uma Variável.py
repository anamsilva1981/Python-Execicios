#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo ')
print(f'O tipo primitivo desse valor é {type(a)}') #Type informa o tipo primitivo 
print(f'Só tem espaços? {a.isspace()}') # Informa se é somente "espaços"
print(f'É numérico {a.isnumeric()}') # Informa se é numerico
print(f'É alfabetico {a.isalpha()}') # Informa se é alfabetico
print(f'É alfanuméricoteste {a.isalnum()}') # Informa se é alfanumérico
print(f'Está em maiúscula {a.isupper()}') #Informe se esta em maiúscula
print(f'Está em minuscula {a.islower()}') # Informa se esta em minuscula
print(f'Esta capitalizada? {a.istitle()}') # Informa se esta capitalizada