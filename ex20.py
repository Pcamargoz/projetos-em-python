from os.path import split

nome = (str(input('Digite o seu nome aqui:')).strip()).upper()
lista = nome.split()
n1 = ('SANTOS' in lista[0])
print(f'o seu nome {n1} contem santos')