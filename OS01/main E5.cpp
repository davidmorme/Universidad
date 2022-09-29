#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

//int Existe(vector <int> T, int x) Es una función que busca el valor x en el vector T, true si sí existe
//bool Dicho(vector <int> T, int x) Es una función que busca el valor x en el vector T con una búsqueda binaria (dichotomique), true si sí existe.
//Para usar Dicho, es necesario que el vector esté organizado de menor a mayor sort(T.begin(), T.end());

/*
// Código que se me ocurrió a mí.
int Existe(vector <int> T, int x){
	for (int i = 0; i <= T.size(); i++){
		if ( T[i] == x ) return true;
	}
	return false;
}
*/

// Código que se le ocurrió al profesor.
int Existe(vector <int> T, int x){
	int i = 0;
	while (i < T.size() && T[i] != x ) i++;
	return i < T.size();
}

bool Dicho(vector <int> T, int x){
	
	int i = 0, j= T.size()-1, k;
	
	while (i <= j){
		k=(i+j)/2;
		if (x == T[k]) return true;
		if (x < T[k]) j=k-1;
		else i = k+1;
	}
	return false;
}


int main() {
	
	vector <int> T; 
	
	double lu;
	do{
		cout << "Tapez un nombre entier, 0 par sortir. ";
		cin >> lu;
		if(lu != 0) T.push_back(lu);
	}while(lu != 0);
	
	int x;
	cout << "Quelle nombre entier vous cherchez? "; cin >> x;
	cout << Existe(T, x);
	
	sort(T.begin(), T.end());
	
	cout << Dicho(T, x);
	return 0;
}