while True:
	slownik = {
	"okno": "window",
	"jabłko": "apple",
	"człowiek": "human",
	"maks": "pantofel",
}

slowo = str(input("Podoaj słowo po polsku: "))
if slowo in slownik:
	print("Słówko po angielsku to: "+slownik[slowo])
else:
	print("Nie ma takiego słówka")
	pytanie = str(input("Czy chcesz dodać słówko do słownika? "))
	if pytanie == "nie":
		break
	elif pytanie == "tak":
		nowe_slowo = str(input("Podaj słowo, które chcesz dodać po angielsku: "))
		slownik[slowo] = nowe_slowo
		print(slownik)
	else:
		print("Niepoprawna odpowiedź")