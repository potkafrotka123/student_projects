from rich.console import Console

console = Console()

licznik = 0

#a = 0

#a = int(input("Podaj temperature: "))

#if a>=-5 and a<10:
	#print("Zima")
#if a>=0 and a<10:
	#print("Przedwiośnie")
#if a>10 and a<15:
	#print("Wiosna")

while licznik < 10:
	z = int(input("Podaj wartość z: "))
	if z==5:
		break
	licznik+=1