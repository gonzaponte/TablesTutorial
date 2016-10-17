
	__kernel void mandelbrot(__global int *output, constant int* maxiter , 
                     constant float* p_size_x, constant float* p_size_y,
                     constant float* min_x, constant float* min_y)
    {
        int row = get_global_id(0);
        int col = get_global_id(1);
        
        int numRows = get_global_size(0);
        int numCols = get_global_size(1);
	
        int gid = col+ row*numCols;
        
        float real, imag, nreal = 0.0f;
        float oreal = min_x[0] + col * p_size_x[0] ;
        float oimag = min_y[0] + row * p_size_y[0] ;
		

        output[gid] = maxiter[0];
       for(int curiter = 0; curiter < maxiter[0]; curiter++) {
           nreal = real*real - imag*imag + oreal;
           imag = 2.0f* real*imag + oimag;
           real = nreal;
		   

		   if ((real*real + imag*imag) >= 4.0f){
                output[gid] = curiter;
				curiter = maxiter[0];
			}
       }
    }