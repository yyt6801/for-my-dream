#include <stdio.h>
#include <tchar.h>
#include <iostream>//system("pause");需要
#include "string.h"//strcpy函数需要
int _tmain(int argc, _TCHAR* argv[])
{
	char aa[]="HelloWorld!";					//char[]
	printf("%s\n",aa);
	printf("%c+%c\n",aa[4],aa[5]);

	char *b=aa;							//char[] -> char*
	printf("%s\n",b);

	const char *c=b;					//char* -> const char*
	printf("%s\n",c);

	char *d;
	d=const_cast<char*>(c);				//const char* -> char*
	printf("%s\n",d);
	strcpy(d,c);						//const char* -> char*
	printf("%s\n",d);

	char *m;
	m="2019-04-18 13:27:08";
	printf("%s\n",m);

	system("pause");

	return 0;

}