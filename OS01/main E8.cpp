#include <iostream>
#include <vector>
#include <algorithm>
#include "compte.h"

using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	return 0;
}

class compte{
	private:
		string numero;
		string titulaire;
		double solde;
		double decouvert;
	public:
		void crediter(double montant);
		void debiter(double montant);
		void afficher();
		compte(string n, string t, double s=0, double d=0);
};
	
		