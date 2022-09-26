#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include "utilities.h"
#include "utilities.cpp"
using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

bool Premier (int n){
	for(int i = 2; i<=sqrt(n);i++) if(n%i == 0) return false;
	return true;
}

int main(int argc, char** argv) {
	int n;
	cout << "Tapez un nombre entier. ";
	cin >> n;
	
	if (Premier(n)){
		cout << "Le nombre " << n << " est premier." << endl;
	}else{
		cout << "Le nombre " << n << " est pas premier." << endl;
	}
	
	cout << "Les nombres premiers entre 1 et 1000: "<< endl;
	for (int i = 1; i <=1000; i++) if(Premier(i)) cout << EI(i,4);
	
	int m;
	cout << endl << "Tapez un nombre entier que vous voulez descomponer. ";
	cin >> m;
	
	
	vector <int> F, E;
	int copie = m;
	
	for (int div = 2; div <=copie;div++){
		if(Premier(div)){
			int exp =0;
			
			while (copie % div ==0){
				exp++;
				copie = copie / div;
			}
			
			if(exp>0){
				F.push_back(div);
				E.push_back(exp);
			}
		}
		if(copie==1) break;
	}
		
	
	cout << endl << "Facteurs :" << endl;
	for (int i =0; i < F.size(); i++) cout << EI(F[i],4);
	cout << endl << "Exp :" << endl;
	for (int i =0; i < F.size(); i++) cout << EI(E[i],4);
	
	
	return 0;
}