#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;


/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {
	int n=5;
	vector <int> T(n);
	
	for(int i = 0; i<n ; i++){
		cout << "Tapez T[" << i << "] ";
		cin >> T[i];
	}
	
	int temp;
	do{
		cout << "Tapez un nombre, 0 par sortir. ";
		cin >> temp;
		if(temp == 0) break;
		T.push_back(temp);
	}while(true);
	
	
	
	
	int minT=T[0];
	int suma=T[0];
	
	for(int i = 1; i < T.size(); i++){
		if(T[i]<minT) minT=T[i];
		suma += T[i];
	}
	int npar=0;
	for(int i = 0; i < T.size(); i++){
		if(T[i]%2 == 0) npar+=1;
	}
	
	double moyen = double(suma)/T.size();
	
	cout << "Le nombre minimum est: " << minT << endl;
	cout << "Le moyen est: " << moyen << endl;
	cout << "Le nombre d'elements pairs est: " << npar << endl;
	
	
	vector <double> U = {0.7412};
	cout << "U[0]: " << U[0] << endl;
	
	for(int i = 1; i < 6 ; i++){
		double b;
		U.push_back(modf(pow(M_PI+U[i-1],5),&b));  // a = pow(M_PI+U[i-1],5); U.push_back(a - trunc(a));
		cout << "U[" << i << "]: " << U[i] << endl;
	}     
	
}