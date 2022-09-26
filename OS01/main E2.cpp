#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include "utilities.h"
#include "utilities.cpp"
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	vector <double> T;
	double lu;
	
	do{
		cout << "Tapez un nombre, 0 par sortir. ";
		cin >> lu;
		if(lu != 0) T.push_back(lu);
	}while(lu != 0);
	
	double suma=T[0];
	double minT=T[0];
	
	for(int i = 1; i < T.size(); i++){
		if(T[i]<minT) minT=T[i];
		suma += T[i];
	}
	double moyen = double(suma)/T.size();
	
	double sumC = 0;
	for(int i = 0; i < T.size(); i++){
		sumC += pow(moyen - T[i],2);
	}
	double Var=sumC/T.size();
	double sd = pow(Var,0.5);
	
	int nEnt=0;
	for(int i = 0; i < T.size(); i++){
		if(T[i]-trunc(T[i]) == 0) nEnt+=1;
	}
	
	cout << "La Moyenne de les nombres est: " << ER(moyen,0,3) << endl;
	cout << "La Variance de les nombres est: " << ER(Var,0,3) << endl;
	cout << "L'ecart type de les nombres est: " << ER(sd,0,3) << endl;
	cout << "Le nombre d'elements entieres est: " << nEnt << endl;
	
	return 0;
}