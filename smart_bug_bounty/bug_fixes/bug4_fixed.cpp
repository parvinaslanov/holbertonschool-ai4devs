#include <iostream>
#include <vector>

// Intended: Dynamically allocate an array, calculate sum, and cleanly deallocate memory
int calculateSum(const int* arr, int size) {
    int sum = 0;
    for (int i = 0; i < size; ++i) {
        sum += arr[i];
    }
    return sum;
}

void processData() {
    int size = 5;
    int* data = new int[size];

    for (int i = 0; i < size; ++i) {
        data[i] = (i + 1) * 10;
    }

    std::cout << "Sum: " << calculateSum(data, size) << std::endl;
    
    // Fix: Properly release dynamically allocated heap array to prevent memory leak
    delete[] data;
}

int main() {
    processData();
    return 0;
}
