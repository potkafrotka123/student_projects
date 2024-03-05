#include <iostream>

using namespace std;

int main(){
	int liczby[9];
	int suma = 0;
	
	for(int i=1; i<11; i++){
		cout<<"Podaj liczbe "<<i<<": ";
		cin>>liczby[i-1];
		}
	
	for(int i=0; i<10; i++){
		suma=suma+liczby[i];
		}
	
	if(suma%2 == 0){
		cout<<"Wynik jest parzysty"<<endl;
		}
	else{
		cout<<"Wynik jest nieparzysty"<<endl;
		}
	
	return 0;
}
