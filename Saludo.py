import sys

nombre = 'Miguel'

def saludar(nombre):
    return f'Hola, {nombre}'

def despedir(nombre):
    return f'Adios, {nombre}'

if __name__ == '__main__':
    print('No me ejecutes, solo soy un modulo')
    print(__name__)
    sys.exit(1)
else:
    print(__name__)