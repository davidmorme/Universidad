#ifndef DJEUN_H
#define DJEUN_H

#include "compte.h"

class djeun : public compte
{
	public:
		void debiter(double montant);
		void afficher();
		djeun(string n, string t, double s, double d, double r=100);
	protected:
		double retmax;
};

#endif