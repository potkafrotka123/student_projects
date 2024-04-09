#Deklarowanie zmiennych
tablica = [0, 0, 0]
suma = 0

#Wczytywanie zmiennych i sumowanie
for i in range(0, 3):
	tablica[i] = int(input('Podaj wartosc '+str(i+1)+': '))
	suma += tablica[i]

#Wypisanie sumy
if suma == 0:
	print('Tablica jest pusta')
else:
	print('Suma wartosci wynosi: '+str(suma))

#Sprawdzanie czy suma jest parzysta
if suma % 2 == 0:
	print('Liczba jest parzysta')
else:
	print('Liczba nie jest parzysta')
