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


// //����windowsAPI--MessageBox
// #include <windows.h>
// //WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PSTR szCmdLine, int iCmdShow)
// int WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PSTR szCmdLine, int iCmdShow)

// {
// 	ShowWindow(FindWindow("ConsoleWindowClass",0),0);//�ó�������ʱ����ʾ���ڿ���̨
// 	int result;
// 	result = MessageBox(NULL, TEXT("�����ҵ�һ�ε���WindowsAPI���--MessageBox--ģ̬�Ի���"), TEXT("ľ�����"), MB_ICONEXCLAMATION | MB_YESNO );//MB_ICONEXCLAMATION | MB_OKCANCEL| MB_ICONQUESTION | MB_DEFBUTTON2
// 	switch(result)
// 	{
// 	//case IDYES: MessageBox(NULL,TEXT( "YOU click yes!"),TEXT("alert"),MB_DEFBUTTON2);
// 	case IDYES: MessageBox(NULL,TEXT( "YOU click yes!"),TEXT("alert"),MB_DEFBUTTON2);
// 	return 0;
// 	case  IDNO: MessageBox(NULL,TEXT( "YOU click NO!"),TEXT("alert"),MB_ICONSTOP);
// 	}
// 	return 0;

// }


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
// #include <stdio.h>
// #include <iostream>
// int main(){
// 	printf("hello_world!");
// 	system("pause");
// }

// #include <stdio.h>
// #include <iostream>
// using namespace std;
// int main(){
// 	// //new ��������飬������ֹ�������--OK
// 	// //��һ�ַ�ʽ  ����һλ����
// 	// double *array;
// 	// array = new double[80*1000];
// 	// //���ʵ�ʱ��*(array+i*y+j)��ʾarray[i][j]
// 	// for(int i=0;i<60;i++){
// 	// 	for(int j=0;j < 1000;j++){
// 	// 		*(array+i*1000+j) = i+j;
// 	// 	}
// 	// }
// 	// cout<<"��¼������CPCRec��ֵ�ɹ���"<<*(array+55*1000+333)<<endl;

// 	//�ڶ��ַ�ʽ ����һ����ά����
// 		double **array1;
// 		array1 = new double *[80];
// 		for(int i=0;i<80;++i)
// 			array1[i] = new double[1000];
// 		//...�õ�ʱ�����ֱ��array1[i][j]
// 		for(int i=0;i<80;i++){
// 			for(int j=0;j < 1000;j++){
// 				array1[i][j] = i+j;
// 			}
// 		}
// 	cout<<"��¼������CPCRec��ֵ�ɹ���"<<array1[50][333]<<endl;
// 	//��ע�⼰ʱdelete
// 		for(int i=0;i<80;++i)
// 			delete[] array1[i];
// 	delete[] array1;
// }


#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    float a=12.257902012398877;
    double b=12.257902012398877;
    const float PI=3.1415926;         // ��������
    cout<<setprecision(15)<<a<<endl;  // ֻ��6-7λ��Ч���֣�����ľͲ���ȷ
    cout<<setprecision(15)<<b<<endl;  // ��15-16λ��Ч���֣�������ȫ��ȷ
    cout<<setprecision(15)<<PI<<endl; 
    return 0;
}