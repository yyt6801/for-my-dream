//test_b.cpp
#include <stdio.h>
#include <iostream>
#include "b.h"
int main(){
	printf("hello_world!bbbbbbbbbbbbbbbbbbbbb\n");
	//extern int add(int,int);
	int x=5;int y=10;
	int z=add(x,y);
	//int z=x+y;
	printf("z's value is %d",z);
	system("pause");
}