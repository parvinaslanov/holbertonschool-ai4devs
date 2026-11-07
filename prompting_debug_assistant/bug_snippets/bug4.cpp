#include <iostream>
#include <vector>

using namespace std;

/**
 * Intended Behavior: Calculate the sum of elements in a vector.
 * Issue Type: Misuse of data types / Unsigned integer underflow
 */
int sumElements(const vector<int>& vec) {
    int total = 0;
    // Bug: Using size_t (unsigned) with i >= 0 causes infinite loop/underflow when empty
    for (size_t i = vec.size() - 1; i >= 0; --i) {
        total += vec[i];
    }
    return total;
}
