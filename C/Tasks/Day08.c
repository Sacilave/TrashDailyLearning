#include <stdio.h>

// P1085 [NOIP2004 普及组] 不高兴的津津
int d8aa() {
    int day = 0, max = 0; int arr[7];
    for (int i = 0; i < 7; i++) {
        int a, b;
        scanf("%d%d", &a, &b);
        arr[i] = a + b;
    }
    for (int i = 6; i >= 0; i--)
    {
        if (arr[i] > 8 && max <= arr[i]) {
            day = i + 1;
            max = arr[i];
        }
    }
    printf("%d", day);
}
