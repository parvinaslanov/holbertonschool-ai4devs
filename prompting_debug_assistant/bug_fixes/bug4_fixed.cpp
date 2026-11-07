#include <iostream>
#include <vector>

using namespace std;

/**
 * Intended Behavior: Calculate the sum of elements in a vector.
 * Issue Type: Misuse of data types / unsigned integer underflow
 */
int sumElements(const vector<int>& vec) {
    int total = 0;
    for (int i = (int)vec.size() - 1; i >= 0; --i) {
        total += vec[i];
    }
    return total;
}
