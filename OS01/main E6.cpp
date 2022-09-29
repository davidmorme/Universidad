#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

typedef vector <vector <double>> matrix;

void mult(matrix A, matrix B, matrix& C){
	int m, n;
	m= A.size();
	n = B[0].size();
	C = matrix (m, vector <double> (n));
	
	for ( int i = 0; i < m; i++){
		for ( int j = 0; j < n; j++ ){
			for ( int k = 0; k < B.size(); k++ ){
				C[i][j] += A[i][k]*B[k][j];
			}
		}
	}
}

int main() {
	
	matrix A, B, C;
	
	A = {{2, 7, 3}, 
		{4, 1, 5}};
	
	B = {{6, 9},
		{3, 2},
		{4, 8}};
	
	mult(A, B, C);
	
	for ( int i = 0; i < C.size(); i++){
		for ( int j = 0; j < C[0].size(); j++ )	cout << C[i][j] << " ";
		cout << endl;
	}
	
	
	return 0;
}