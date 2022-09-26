#include <iostream>
#include <cmath>
#include <vector>
using namespace std;


int main() {
	int a = 2;
	a = pow(2,5);
	string tout = to_string(a)+ "Hola \n";
	cout << tout;
	
	int i=5, j=2;
	double x=5.0, y=2.0, z=2.5;
	x=i/2.0; //Si no le pongo el .0 me lo coge como una division de enteros porque i es entero
	x=z/2; //Si no le pongo el .0 no importa porque z es doble
	
	bool V=true;
	
	cout<< (x>y);
	cout<< x;
	cout<< V;

	
	int n = 1000, p = 1;
	
	tout = "\n n = " + to_string(n)+ "\n p = "+ to_string(p);
	cout << tout;
	
	int b=1;
	if (a > 3 && b == 1) x = 2*y;
	
	
	for (int i = 0; i < 5; i++) {
		cout << i << "\n";
	}
	
	int s = 3;
	for (int i=1; i<=10; i++) s = s+i;
	
	for (i=1; i<=10; i++){
		s = s+i;
		cout << i;
	}
	
	int e;
	for (int i = 1; i <= 10; i++) {
		cout << "Taper un entier, 0 pour finir : "; cin >> e;
		cout << "Vous avez tapé " << e << endl;
		if (e == 0) break;
	}
	
	vector <double> U (10); // Vecteur de 10 réels
	vector <int> vect (20,30); // 20 entiers initialisés à 30
	
	U[1] = 3.5; cout << U[2] << vect[0]<< endl; // Indices entre crochets comme en C
	
	U.push_back(100);
	for (double x : U)
        cout << x << " ";
	
	cout << endl << U.back();
	
	U.pop_back();
	cout << endl << U[10] << endl;
	for (double x : U)
        cout << x << " ";
    
	U.push_back(50);
    cout << endl << U[10] << endl;
    
    vector <vector<int>> M (2, vector<int> (3)); //Matrice 2x3 d'entiers
    
    cout << M[0][0];
    
	return 0;
	
}