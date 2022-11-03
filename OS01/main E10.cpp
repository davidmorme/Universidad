#include <iostream>
#include <string>

using namespace std; 

/* run this program using the console pauser or add your own getch, system("pause") or input loop */


bool palindrome(string mot){
	int n=mot.length();
	
	for( int i=0; i < n/2 ; i++){
		if(mot[i]!=mot[n-i-1]){
			cout << mot << " Ce n'est pas palindrome" <<endl;
			return false;
		}
	}
	cout << mot << " C'est palindrome" <<endl;
	return true;
}

int main(int argc, char** argv) {
	palindrome("anna");
	palindrome("javier");
	return 0;
}