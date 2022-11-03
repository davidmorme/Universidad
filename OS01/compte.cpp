#include "compte.h"
#include <iostream>
#include <string>
using namespace std;

compte::compte(string n, string t, double s, double d){
	numero = n;
	titulaire = t;
	solde = s;
	decouvert = d;
} 
void compte::crediter(double montant){
	solde += montant;
}
void compte::debiter(double montant){
	if(solde - montant >= -decouvert){
		solde -= montant;
	}else{
		cout << "Debito de "<< montant << " no permitido, saldo insuficiente"<< endl;
	}
	
}
void compte::afficher(){
	cout << "Compte: " << numero << endl;
	cout << "Titulaire: " << titulaire << endl;
	cout << "Solde: " << solde << endl;
	cout << "Decouvert: " << decouvert << endl;
}
