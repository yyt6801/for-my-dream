////获取文件 1.txt的内容
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
//	if(in) // 有该文件  
//	{  
//		while ( getline( ifile, linewords, '\n' ) )
//		while (getline (in, line)) // line中不包括每行的换行符  
//		{   
//			cout << line << endl;  
//			if(line>100)
//				cout << "small" << endl;
//			else
//				cout << "big" <<endl;
//		}  
//	}  
//	else // 没有该文件  
//	{  
//		cout <<"no such file" << endl;  
//	}  
//
//	system ("pause");
//	return 0;  
//}  


//调用windowsAPI--MessageBox
//#include <windows.h>
////WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PSTR szCmdLine, int iCmdShow)
//int WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PSTR szCmdLine, int iCmdShow)
//
//{
//	int result;
//	result = MessageBox(NULL, TEXT("这是我第一次调用WindowsAPI编程--MessageBox--模态对话框！"), TEXT("木马程序！"), MB_ICONEXCLAMATION | MB_YESNO );//MB_ICONEXCLAMATION | MB_OKCANCEL| MB_ICONQUESTION | MB_DEFBUTTON2
//	switch(result)
//	{
//	case IDYES: MessageBox(NULL,TEXT( "YOU click yes!"),TEXT("alert"),MB_DEFBUTTON2);
//	case  IDNO: MessageBox(NULL,TEXT( "YOU click NO!"),TEXT("alert"),MB_ICONSTOP);
//	}
//	return 0;
//
//}


//使用strncpy(sub,string+12,13)/*将string中从string[12]开始的13个数字复制到sub中*/
#include <iostream>
#include "string.h"
using namespace std;
int main()
{
	#define size 200//
	char a[size];
	memset(a,0x00,sizeof(a));
	char string[25]= "2007-12-20 18:31:34:123";
	strncpy(a,string,19);
	cout<<a<< endl;
	system ("pause");
	return 0;  

}


// //通过互斥对象句柄检测程序是否运行
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
// 			cout << "输入互斥对象的名称:" << endl;
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