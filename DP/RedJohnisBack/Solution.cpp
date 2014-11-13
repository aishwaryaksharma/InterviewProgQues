#include <iostream>
#include <malloc.h>
using namespace std;

bool IsPrime(int num)
{
    for (int i=2; i<=num/2; i++)
        if (!(num % i))
            return false;
    return true;
}

void FillArray(int **DP_Array, int N)
{
    DP_Array[0][0] = 1;
    DP_Array[0][1] = 0;
    int cur = 1;
    while (cur < N) {
        DP_Array[cur][0] = DP_Array[cur-1][0] + (cur+1)/4;
        DP_Array[cur][1] = DP_Array[cur-1][1];
        for (int i=DP_Array[cur-1][0]+1; i<=DP_Array[cur][0]; i++)
            if (IsPrime(i))
                ++DP_Array[cur][1];
        cur++;
    }
    return;
}

int main() {
    /* Declarations */
    int T = 0;
    int N = 0;
    int ret = 0;
    int **DP_Array = NULL;

    ret = scanf("%d", &T);
    for (int i=0; i<T; i++) {
        ret = scanf("%d", &N);
        DP_Array = int **)malloc(N * sizeof(int *));(
        for (int j=0; j<N; j++)
            DP_Array[j] = (int *) malloc (2 * sizeof(int));

        FillArray(DP_Array, N);
        cout << DP_Array[N-1][1] << endl;
    }
    return 0;
}

