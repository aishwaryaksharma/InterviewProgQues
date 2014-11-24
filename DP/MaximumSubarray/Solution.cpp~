#include <iostream>
#include <malloc.h>
#include <stdarg.h>

using namespace std;

static int
GetMaxContinuous(int *A, int N)
{
   int maxContinuous = 0;

   /* Initialize */
   int maxSoFar = A[0];
   int maxEndingHere = A[0] > 0 ? A[0] : 0;

   /* Calculate */
   for (int dp = 1; dp < N; dp++) {
      maxEndingHere = maxEndingHere + A[dp];
      maxEndingHere = maxEndingHere > 0 ? maxEndingHere : 0;
      maxSoFar = maxSoFar > maxEndingHere ? maxSoFar : maxEndingHere;
   }

   maxContinuous = maxSoFar;

   return maxContinuous;
}

int main()
{
   int T = 0;
   int N = 0;
   int *A = NULL;
   int n = 0;

   n = scanf("%d", &T);
   for (int t = 0; t < T; t++) {
      int maxContinuous = 0;
      int maxNoncontinuous = 0;

      n = scanf("%d", &N);

      /* Allocate memory for array */
      A = (int *)malloc(N * sizeof(int));
      if (!A) {
         printf("Error: Memory allocation failed for array;\n");
      }

      for (int a = 0; a < N; a++) {   
         n = scanf("%d", &A[a]);
      }

      for (int a = 0; a < N; a++) {
         if (0 < A[a]) {
            maxNoncontinuous += A[a];
         }
      }

      maxContinuous = GetMaxContinuous(A, N);

      printf("%d %d\n", maxContinuous, maxNoncontinuous);

      /* Free allocated memory */
      free(A);
   }
}
