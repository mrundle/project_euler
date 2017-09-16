/*
 * The prime factors of 13195 are 5, 7, 13 and 29. 
 * What is the largest prime factor of the number 600851475143 ?
 */
#include "project_euler_lib.h"
#define INPUT 600851475143U
#define SOLUTION 6857U

size_t
largest_prime_factor(size_t n)
{
    for (size_t i = 2; i < n; i++) {
        if (n % i == 0) {
            return largest_prime_factor(n / i);
        }
    }
    // no prime factors
    return n;
}


size_t
solution(void)
{
    return largest_prime_factor(INPUT);
}

MAIN(solution, SOLUTION);
