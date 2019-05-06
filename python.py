print('Write the amount of numbers u want to sum up and square it: ')
ilosc= int(input())
lista = []
def pobierz_dane(liczba_cyfr):
    for i in range(liczba_cyfr):
        cyfry = int(input('Give me a number: '))
        lista.append(cyfry)
    return lista
wynik = pobierz_dane(ilosc)
print(wynik)

def suma_kwadrat(list, size):
   if (size == 0):
     return 0
   else:
     return list[size - 1] + suma_kwadrat(list, size - 1)

total = suma_kwadrat(lista, len(lista))**2

print("Total is: ", total)
