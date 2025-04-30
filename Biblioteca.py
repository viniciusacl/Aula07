def imprime_nome(nome):
    print(f"nome:{nome}")

def Piramide(n):
    n = 5
    for x in range(1, n + 1):
        for y in range(0, x):
            print(x, end=" ")
        print()

def contar_vogais(texto):
    contador = 0
    for x in range(len(texto)):
       if texto[x] == 'a' or texto[x] == 'e' or texto[x] == 'i' or texto[x] == 'o' or texto[x] == 'u':
           contador += 1
    print(contador)

def estoque (item, quantidade, valor_unit):
    valortotal = quantidade * valor_unit
    return valortotal

def numero(n):
    if n == 0:
        return "Z"
    elif n > 0:
        return "P"
    else:
        return "N"

def soma(*a):
    soma = 0
    for x in range(len(a)):
        soma += a[x]
    print(soma)