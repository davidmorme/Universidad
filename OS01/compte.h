#ifndef COMPTE_H
#define COMPTE_H
#include <string>
using namespace std;

class compte{
	protected:
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

#endif