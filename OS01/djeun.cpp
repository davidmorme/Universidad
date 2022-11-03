
#include "djeun.h"


#include <iostream>
#include <string>
using namespace std;

djeun::djeun(string n, string t, double s, double d, double r):compte(n, t, s, d){
	retmax = r;
}

void djeun::debiter(double montant){
	if(solde - montant >= -decouvert){
		if(montant <= retmax ){
			solde -= montant;
		}else{
			cout << "Debito de "<< montant << " no permitido, excede maximo por retiro."<< endl;
		}		
	}else{
		cout << "Debito de "<< montant << " no permitido, saldo insuficiente."<< endl;
	}
	
}
void djeun::afficher(){
	compte::afficher();
	cout << "Montant maximum pour chaque retrait: " << retmax << endl;
}