#include <stdio.h>
#include <assert.h>
#include <stdbool.h>
#include <string.h>

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

// failure to do something intelligent
// breaks for numbers with inner zeroes
bool
is_palindrome_broken(unsigned n) {
	if (n < 10) {
		return true;
	}

	// get the least significant (trailing) number
	unsigned lsn = n % 10;

	// get the most significant (leading) number
	unsigned power = 1;
	while (n > power) {
		power *= 10;
	}
	power /= 10;
	unsigned msn = n / power;

	// get the remainder
	unsigned rem = n - lsn;
	rem -= msn * power;
	rem /= 10;

	printf("in  = %u\n", n);
	printf("msn = %u\n", msn);
	printf("lsn = %u\n", lsn);
	printf("rem = %u\n", rem);

	return lsn == msn && is_palindrome(rem);
}

int main(void) {
	// positive
	assert(is_palindrome(0));
	assert(is_palindrome(9));
	assert(is_palindrome(101));
	assert(is_palindrome(906609));
	assert(is_palindrome(1234321));

	// negative
	assert(!is_palindrome(12));
	assert(!is_palindrome(122));
	assert(!is_palindrome(9994499));

	printf("OK\n");
}
