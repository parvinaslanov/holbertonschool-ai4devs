#include <stdio.h>

int main(void) {
    int values[] = {2, 4, 6, 8, 10, 12};
    size_t count = sizeof(values) / sizeof(values[0]);

    printf("Count: %zu\n", count);
    for (size_t i = 0; i < count; i++) {
        printf("%d\n", values[i]);
    }

    return 0;
}
