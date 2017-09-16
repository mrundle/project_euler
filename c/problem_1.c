/* https://projecteuler.net/problem=1
 * 
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we
 * get 3, 5, 6 and 9. The sum of these multiples is 23.
 *
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */
#include "project_euler_lib.h"
#define SOLUTION 233168

static size_t
solution(void)
{
    size_t result = 0;
    for (size_t i = 3; i < 1000; i++) {
        if (i % 3 == 0 || i % 5 == 0) result += i;
    }
    return result;
}

MAIN(solution, SOLUTION);
