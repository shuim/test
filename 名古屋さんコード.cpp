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


		

}