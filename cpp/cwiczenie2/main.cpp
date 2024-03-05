#include <iostream>

using namespace std;

int main(){
	int liczba = 0;
	int suma = 0;
	
	cout<<"Podaj 10 liczb calkowitych"<<endl;
	
	for(int i=1; i<11; i++){
		cout<<"Podaj liczbe "<<i<<": ";
		cin>>liczba;
		suma = suma+liczba;
		}
	
	if(suma%2 == 0){
		cout<<"Wynik jest parzysty"<<endl;
		}
	else{
		cout<<"Wynik jest nie parzysty"<<endl;
		}
	
	return 0;
}
