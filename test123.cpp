////��ȡ�ļ� 1.txt������
//#include <stdlib.h>
//#include <fstream>  
//#include <string>  
//#include <iostream>  
//using namespace std;  
//
//int main()  
//{  
//	ifstream in("1.txt");  
//	string filename;  
//	string line;  
//
//	if(in) // �и��ļ�  
//	{  
//		while ( getline( ifile, linewords, '\n' ) )
//		while (getline (in, line)) // line�в�����ÿ�еĻ��з�  
//		{   
//			cout << line << endl;  
//			if(line>100)
//				cout << "small" << endl;
//			else
//				cout << "big" <<endl;
//		}  
//	}  
//	else // û�и��ļ�  
//	{  
//		cout <<"no such file" << endl;  
//	}  
//
//	system ("pause");
//	return 0;  
//}  


//����windowsAPI--MessageBox
//#include <windows.h>
////WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PSTR szCmdLine, int iCmdShow)
//int WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PSTR szCmdLine, int iCmdShow)
//
//{
//	int result;
//	result = MessageBox(NULL, TEXT("�����ҵ�һ�ε���WindowsAPI���--MessageBox--ģ̬�Ի���"), TEXT("ľ�����"), MB_ICONEXCLAMATION | MB_YESNO );//MB_ICONEXCLAMATION | MB_OKCANCEL| MB_ICONQUESTION | MB_DEFBUTTON2
//	switch(result)
//	{
//	case IDYES: MessageBox(NULL,TEXT( "YOU click yes!"),TEXT("alert"),MB_DEFBUTTON2);
//	case  IDNO: MessageBox(NULL,TEXT( "YOU click NO!"),TEXT("alert"),MB_ICONSTOP);
//	}
//	return 0;
//
//}


//ʹ��strncpy(sub,string+12,13)/*��string�д�string[12]��ʼ��13�����ָ��Ƶ�sub��*/
// #include <iostream>
// #include "string.h"
// using namespace std;
// int main()
// {
// 	#define size 200//
// 	char a[size];
// 	memset(a,0x00,sizeof(a));
// 	char string[25]= "2007-12-20 18:31:34:123";
// 	strncpy(a,string,19);
// 	cout<<a<< endl;
// 	system ("pause");
// 	return 0;  

// }


// //ͨ������������������Ƿ�����
// #include <stdio.h>
// #include <Windows.h>
// #include <iostream>
// using namespace std;

// char IPname[20];
// 	BOOL IsAlreadyRun()
// 	{
// 		HANDLE hMutex = NULL;
// 		hMutex = ::CreateMutex(NULL, FALSE, IPname);
// 		if (hMutex)
// 		{
// 			if(ERROR_ALREADY_EXISTS == ::GetLastError())
// 			{
// 				return TRUE;
// 			}
// 		}
// 		return FALSE;


// 	}
// 	int	main()
// 	{
// 		while(1)
// 		{
// 			cout << "���뻥����������:" << endl;
// 			cin >> IPname;
// 			if(IsAlreadyRun())
// 			{
// 				printf("alreadyRun!!!");
// 			}
// 			else 
// 			{
// 				printf("NOTALREADYRUN!!!!");
// 			}
// 		}
// 	}

//�򵥲��Դ�ӡ��Hello_world!!!
#include <stdio.h>
#include <iostream>
int main(){
	printf("hello_world!");
	system("pause");
}