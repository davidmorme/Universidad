#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include "utilities.h"
#include "utilities.cpp"
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

double Moyenne(vector <double> T){
	double somme=0;
	for(int i = 0; i < T.size(); i++) somme += T[i];
	return somme/T.size();
}

double Variance(vector <double> T){
	double moyenne=Moyenne(T);
	double sommeC = 0;
	for(int i = 0; i < T.size(); i++) sommeC += pow(moyenne - T[i],2);
	return sommeC/T.size();
}

double Ecart_type(vector <double> T){
	return sqrt(Variance(T));
}

int Element_entier(vector <double> T){
	int nEnt=0;
	for(int i = 0; i < T.size(); i++){
		if(T[i] == trunc(T[i])) nEnt++;
	}
	return nEnt;
}


int main(int argc, char** argv) {
	int n; RandGen G; 
	cout << "Entrez le nombre de numeros que vous souhaitez generer. "; cin >> n;
	vector <double> T(n);
	
	for (int i = 0; i < T.size(); i++) T[i]=G.RandReal (0,100);
	
	cout << "La Moyenne de les nombres est: " << ER(Moyenne(T),0,3) << endl;
	cout << "La Variance de les nombres est: " << ER(Variance(T),0,3) << endl;
	cout << "L'ecart type de les nombres est: " << ER(Ecart_type(T),0,3) << endl;
	cout << "Le nombre d'elements entieres est: " << Element_entier(T) << endl;
	
	return 0;
}