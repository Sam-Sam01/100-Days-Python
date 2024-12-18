#include <stdio.h>

int main() {
    int n, stu_height[n];
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) {
        scanf("%d", &stu_height[i]);
    }

    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += stu_height[i];
    }
    
    int avg = sum / n;
    printf("Average height: %d\n", avg);
}