def zapisywanie_danych(text):
	with open("plik.txt", "a+") as plik:
		plik.write(text)

def wczytywanie_danych():
	with open("plik.txt", "r") as plik:
		for linia in plik:
			print(linia.strip())

#Wpisywanie danych
text = input("Podaj tekst, który chcesz zapisać: ")
zapisywanie_danych(text)

#Odczytywanie danych
print("Oto zapisany tekst w pliku: ")
wczytywanie_danych()
