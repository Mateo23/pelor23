def dodawanie(a, b):
    return a + b

def get_info():
    print('To jest prosty programik kalkulator')

get_info()

print('Podaj pierwszą liczbę:')
a = int(input())
print('Podaj druga liczbę:')
b = int(input())

print(dodawanie(a, b))
