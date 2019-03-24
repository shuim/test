#include<iostream>
#include<cstdlib>
#include<stdio.h>
#include<math.h>
# define m 4
# define n 5
# define l 2

int main(){
	double X[m][n]={{1.0,1.0,2.0,3.0,1.0},
	                {0.0,1.0,0.0,1.0,1.0},
	                {2.0,0.0,4.0,4.0,0.0},
	                {3.0,0.0,6.0,6.0,0.0}};
	double U[m][l], V[l][n], XV[m][n], Phi[m][n][l];
	double U_ex[m][l] = {{1.0,1.0},
	                     {0.0,1.0},
	                     {2.0,0.0},
	                     {3.0,0.0}};
	double V_ex[l][n] = {{1.0,0.0,2.0,2.0,0.0},
	                     {0.0,1.0,0.0,1.0,1.0}};
	double sum, eps = 1.e-15;
	printf("X matrix\n");
	for(int i=0; i<m; ++i){
      for(int j = 0; j<n; ++j){
		printf("%5.2f",X[i][j]);
	  }
	  printf("\n");
	}
	srand((unsigned)time(NULL)); 
	for(int i=0;i<m;++i){
		for(int k=0;k<l;++k){
			double r = (double) rand()/RAND_MAX;
			U[i][k] = r;
		}
	}
	for(int k = 0;k<l;++k){
		for(int j = 0;j<n;++j){
			double r = (double)rand()/RAND_MAX;
			V[k][j] = r;
		}
	}
	for(int i = 0;i<m;++i){
		for(int j = 0;j<n;++j){
			for(int k=0;k<l;++k){
				Phi[i][j][k] = 0.0;
			}
		}
	}

    for(int it=0;it<100;++it){
	  for(int j=0;j<n;++j){
		for(int i=0;i<m;++i){
		  sum=0.0;
		  for(int k = 0;k<l;++k){
			sum+= U[i][k]*V[k][j];
		  }
		  XV[i][j] = sum;
		}
	}
	double error = 0.0;
	for(int j = 0;j<n;++j){
	  for(int i=0;i<m;++i){
		error += pow(XV[i][j] - X[i][j],2);
	  }
	}
	error = sqrt(error);
	if(error < eps) break;
	printf("it=%d error = %5.3e\n", it, error);
	for(int i=0;i<m;++i){
		for(int j = 0;j<n;++j){
			for(int k = 0;k<l;++k){
				if(XV[i][j]!=0.0)Phi[i][j][k] = U[i][k] * V[k][j] / XV[i][j];
			}
		}
	}
	for(int i=0;i<m;++i){
		for(int k = 0;k<l;++k){
			double sum1 = 0.0;
			double sum2 = 0.0;
			for(int j = 0;j<n;++j){
				sum1 += V[k][j];
				sum2 += X[i][j] * Phi[i][j][k];
			}
			if(sum1 !=0.0) U[i][k] = sum2/sum1;
		}
	}
	for(int i = 0;i<m;++i){
		for(int j = 0;j<n;++j) {
			sum = 0.0;
			for(int k = 0;k<l;++k){
				sum+= U[i][k]*V[k][j];
			}
			XV[i][j] = sum;
		}
	}
	for(int i = 0;i<m;++i){
		for(int j = 0;j<n;++j){
			for(int k = 0;k<l;++k){
				if(X[i][j] != 0.0)Phi[i][j][k] = U[i][k] * V[k][j] / XV[i][j];
			}
		}
	}
	for(int k = 0;k<l;++k){
		for(int j = 0;j<n;++j){
			double sum1 = 0.0;
			double sum2 = 0.0;
			for(int i = 0;i<m;++i){
				sum1 += U[i][k];
				sum2 += X[i][j] * Phi[i][j][k];
			}
			if(sum1 != 0.0)V[k][j] = sum2/sum1;
		}
	}
}
    double Usum = 0.0;
    double Usum_ex = 0.0;
    printf("U_matrix\n");
    for(int i = 0;i<m;++i){
		for(int k = 0;k<l;++k){
			printf("%5.2f", U_ex[i][k]);
		}
		printf("\n");
	}
	printf("\n");
	for(int i = 0;i<m;++i){
		for(int k = 0;k<l;++k){
			printf("%5.2f",U[i][k]);
			Usum += pow(U[i][k],2);
			Usum_ex += pow(U_ex[i][k],2);
		}
		printf("\n");
	}
	double Vsum = 0.0;
	double Vsum_ex = 0.0;
	printf("V_matrix\n");
	for(int k = 0;k<l;++k){
		for(int j = 0;j<n;++j){
			printf("%5.2f",V_ex[k][j]);
		}
		printf("\n");
	}
	printf("\n");
	for(int k = 0;k<l;++k){
		for(int j = 0;j<n;++j){
			printf("%5.2f",V[k][j]);
			Vsum += pow(V[k][j],2);
			Vsum_ex += pow(V_ex[k][j],2);
		}
		printf("\n");
	}
	sum = sqrt(Usum + Vsum);
	double sum_ex = sqrt(Usum_ex + Vsum_ex);
	printf("%5.3f %5.3f \n", sum_ex, sum);

}