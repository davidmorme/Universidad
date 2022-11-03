#include "compte.h"

compte::compte(string n, string t, double s=0, double d=0){
	numero = n;
	titulaire = t;
	solde = s;
	decouvert = d;
} 
void compte::crediter(double montant){
	solde += montant;
}
void compte::debiter(double montant){
	solde -= montant;
}
void compte::afficher(){
	cout << "Compte: " << numero << endl;
	cout << "Titulaire: " << titulaire << endl;
	cout << "Solde: " << solde << endl;
	cout << "Decouvert: " << decouvert << endl;
}
