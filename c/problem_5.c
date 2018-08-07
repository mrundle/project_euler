/*
 * Project Euler - Problem 5
 *
 * Generated automatically via the 'pull' script
 * in this directory.
 *
 *  2520 is the smallest number that can be divided by each
 *  of the numbers from 1 to 10 without any remainder. What
 *  is the smallest positive number that is evenly divisible
 *  by all of the numbers from 1 to 20?
 */
#include "project_euler_lib.h"

#define SOLUTION 232792560

#include <stdbool.h>

// unoptimized
size_t
solution(void)
{
	for (unsigned i = 20;; i+=20) {
		bool found = true;
		for (unsigned j = 19; j >= 3; j--) {
			if (i % j != 0) {
				found = false;
				break;
			}
		}
		if (found) {
			return i;
		}
	}
    return 0;
}

MAIN(solution, SOLUTION);
