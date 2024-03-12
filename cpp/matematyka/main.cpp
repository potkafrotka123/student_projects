#include <iostream>
#include "CppConsoleTable.hpp"

using namespace std;
using ConsoleTable = samilton::ConsoleTable;

int main(){
	cout<<"Program matematyczny v.beta"<<endl;
	ConsoleTable table(1, 2, samilton::Alignment::centre);
	table[0][0] = "Test";
	ConsoleTable::TableChars chars;
	chars.centreSeparation = '+';
	table.setTableChars(chars);
	cout<<table;
	return 0;
}
