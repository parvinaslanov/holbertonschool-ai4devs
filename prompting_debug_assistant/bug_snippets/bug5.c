/* Bug 5: Count and print all elements in an integer array. */
#include <stdio.h>

int main(void) {
    int values[] = {4, 8, 15, 16, 23, 42};
    int count = sizeof(values[0]) / sizeof(values);

    printf("Number of values: %d\n", count);
    printf("Array contents: ");

    for (int i = 0; i < count; i++) {
        printf("%d ", values[i]);
    }

    printf("\n");
    return 0;
}
