#include <stdio.h>
#include "../common/book.h"
 /*
     Beginner Example of Using CUDA Programming. 
     The important distinction for this example is separating the CPU and the system memory (host) and the GPU and its memory (device) 
*/

//Global keyword executes function of the device (GPU)
//These functions: must return void, are called using <<<grid, block>>> syntax and can access global, shared, and local GPU memory

__global__ void add(int a, int b, int *c){
    *c = a + b;
}
int main(void)
{
   int c;
   int* dev_c;

   //Allocation of memory buffer for the result
   HANDLE_ERROR(cudaMalloc((void**) &dev_c, sizeof(int)));

   //Calling of cuda function with __global__
   add<<<1,1>>>(2,7,dev_c);

   //Allocate memory back onto the host
   HANDLE_ERROR(cudaMemcpy(&c, dev_c, sizeof(int), cudaMemcpyDeviceToHost));
   
   printf("2 + 7 = %d\n", c);
   cudaFree(dev_c);

    return 0;
}