/*
 * Project Euler - Problem 4
 *
 * Generated automatically via the 'pull' script
 * in this directory.
 *
 *  A palindromic number reads the same both ways. The largest
 *  palindrome made from the product of two 2-digit numbers is
 *  9009 = 91 × 99. Find the largest palindrome made from the
 *  product of two 3-digit numbers.
 */
#include "project_euler_lib.h"

#define SOLUTION 906609

bool
is_palindrome(unsigned n) {
	if (n < 10) return true;

	char str[8];
	sprintf(str, "%u", n);	
	unsigned len = strlen(str);

	for (unsigned i = 0; i < len / 2; i++) {
		if (str[i] != str[len - 1 - i]) {
			return false;
		}
	}
	return true;
}

size_t
solution(void)
{
	unsigned sol = 0;
	for (unsigned i = 1000; i >= 100; i--) {
		for (unsigned j = i; j >= 100; j--) {
			unsigned n = i * j;
			if (n > sol && is_palindrome(n)) {
				sol = n;
			}
		}
	}
	return sol;
}

MAIN(solution, SOLUTION);
