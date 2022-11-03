#include <iostream>
#include <vector>
#include <algorithm>
#include "compte.h"
#include "djeun.h"

using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {
	compte c1("C001", "PRINS", 1000, 100);
	compte c2("C002", "FONTENAY");
	
	c1.crediter(100);
	c1.debiter(50);
	c1.afficher();
	
	c2.debiter(50);
	c2.afficher();
	
	djeun c3("C003", "MORA", 1000, 100, 50);
	c3.crediter(100);
	c3.debiter(75);
	c3.afficher();
	
	return 0;
}

	
		