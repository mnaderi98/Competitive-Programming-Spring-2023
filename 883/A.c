#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);
    
    // x > y cut
    for (int i = 0; i < t; i++) {
        int n;
        scanf("%d", &n);
        int res = 0;
        
        for (int j = 0; j < n; j++) {
            int x, y;
            scanf("%d %d", &x, &y);
            
            if (x > y) {
                res += 1;
            }
        }
        
        printf("%d\n", res);
    }
    
    return 0;
}
