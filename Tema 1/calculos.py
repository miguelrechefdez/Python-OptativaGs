import sys

if __name__ == '__main__':
    print('No me ejecutes, solo soy un modulo')
    print(__name__)
    sys.exit(1)
else:
    print(__name__)

def suma(a, b):
    return (a+b)

def resta(a, b):
    return (a-b)