
#include <windows.h>

//�������ڹ��̺���

LRESULT CALLBACK WndProc(HWND,UINT,WPARAM,LPARAM);

//����һ��ȫ�ֱ�������Ϊ��������

TCHAR szClassName[] = TEXT("SimpleWin32");

//Ӧ�ó���������

int WINAPI WinMain (HINSTANCE hInstance,
					HINSTANCE hPrevInstance,
					LPSTR szCmdLine,
					int iCmdShow)
{

	//������
	WNDCLASS wndclass;

	//������ˮƽ����Ŀ�Ⱥʹ�ֱ����ĸ߶ȱ仯ʱ�ػ���������
	wndclass.style = CS_HREDRAW|CS_VREDRAW;

	//�������ڹ��̺���
	wndclass.lpfnWndProc = WndProc;
	wndclass.cbClsExtra = 0;
	wndclass.cbWndExtra = 0;
	wndclass.hInstance = hInstance;//ʵ�����
	wndclass.hIcon = LoadIcon(NULL,IDI_APPLICATION);//ͼ��
	wndclass.hCursor = LoadCursor(NULL,IDC_ARROW);//���
	wndclass.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);//��ˢ
	wndclass.lpszMenuName  = NULL;//�˵�
	wndclass.lpszClassName = szClassName;//������

	//ע�ᴰ����
	if(!RegisterClass (&wndclass))
	{
		MessageBox (NULL, TEXT ("RegisterClass Fail!"), 
			szClassName, MB_ICONERROR);
		return 0;
	}



	//��������
	HWND hwnd;
	hwnd = CreateWindow(szClassName,//����������
	
		TEXT ("���ڲ��Գ���"),//���ڱ��� 
		WS_OVERLAPPEDWINDOW,//���ڷ��,��ͨ������ʹ�õ�windows������ʽ
		CW_USEDEFAULT,//ָ�����ڵĳ�ʼˮƽλ��,����Ļ����ϵ�Ĵ��ڵ����Ͻǵ�X����
		CW_USEDEFAULT,//ָ�����ڵĳ�ʼ��ֱλ��,����Ļ����ϵ�Ĵ��ڵ����Ͻǵ�Y����
		CW_USEDEFAULT,//���ڵĿ��
		CW_USEDEFAULT,//���ڵĸ߶�
		NULL,//�����ھ��
		NULL,//���ڲ˵����
		hInstance,//ʵ�����
		NULL);

	ShowWindow(hwnd,iCmdShow);//��ʾ����
	UpdateWindow(hwnd);//������ʾ����

	////��Ϣѭ����ʽ1
	//MSG msg;
	//while(GetMessage(&msg,NULL,0,0))//����Ϣ������ȡ��Ϣ 
	//{
	//	TranslateMessage (&msg);              //ת����Ϣ
	//	DispatchMessage (&msg);               //�ɷ���Ϣ
	//}
	//return msg.wParam;

	////��Ϣѭ����ʽ2
	MSG msg;
	while(true)
	{
		if(PeekMessage(&msg,NULL,0,0,PM_REMOVE)) //����Ϣ������ȡ��Ϣ
		{
			if(msg.message == WM_QUIT)
				break;
			TranslateMessage (&msg);           //ת����Ϣ
			DispatchMessage (&msg);            //�ɷ���Ϣ
		}
		else
			WaitMessage();

	} //End of while(true)
}

//��Ϣ������

//����:���ھ������Ϣ����Ϣ��������Ϣ����

LRESULT CALLBACK WndProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
	//�������Ȥ����Ϣ
	switch (message)
	{
		case WM_CREATE: CreateWindow(TEXT("BUTTON"), //�ؼ�"������" 
			TEXT("��ť(&A)"), 
			WS_CHILD | WS_VISIBLE |BS_PUSHBUTTON, //�ؼ���ʽ��BS_PUSHBUTTON   BS_DEFPUSHBUTTON   BS_CHECKBOX   BS_AUTOCHECKBOX   BS_RADIOBUTTON   BS_3STATE   BS_AUTO3STATE
			10, 10, 100, 30, hwnd, 
			(HMENU)1000, //�ؼ�ID 
			((LPCREATESTRUCT) lParam)->hInstance, //ʵ����� 
			NULL); 
		return 0; 
		case WM_DESTROY:
			PostQuitMessage(0);
		return 0;
		
		//���û��رմ��ڣ��������٣���������������˳���Ϣ�����˳���Ϣѭ��
		
	}
	//������Ϣ������ϵͳ�ṩ��ȱʡ������
	return ::DefWindowProc (hwnd, message, wParam, lParam);
}

////��������������������˧���ķָ��ߡ������������������C 
//#include <Windows.h>
//
///*
//* ���ڵĻص�����
//*/
//LRESULT CALLBACK WindowProc(HWND hwnd,      // handle to window
//    UINT uMsg,      // message identifier
//    WPARAM wParam,  // first message parameter
//    LPARAM lParam)   // second message parameter
//{
//    HDC hDC;
//	PAINTSTRUCT ps;
//
//	//paint�е��ı�����
//	char painttest[30]="welcome to yyt6801's virus";
//    switch (uMsg)
//    {
//    case WM_PAINT:
//        /*
//         * �����ػ�ʱ����
//         * ֻ����WM_PAINT��Ϣ�вſ���ʹ��BeginPaint��EndPaint
//         * ������Ϣʹ��GetDC��ReleaseDC
//         */
//        hDC = BeginPaint(hwnd, &ps);
//        TextOut(hDC, 0, 50, painttest, strlen(painttest));
//        EndPaint(hwnd, &ps);
//        break;
//    case WM_CHAR:
//        MessageBox(hwnd, "WM_CHAR��Ϣ������", "��ʾ", MB_OK);
//        break;  
//    case WM_LBUTTONDOWN:
//        hDC = GetDC(hwnd);
//        TextOut(hDC, 0, 70, "onclick", strlen("onclick"));
//        ReleaseDC(hwnd, hDC);
//        break;
//    case WM_CLOSE:
//        if (IDYES == MessageBox(hwnd, "ȷ��Ҫ�˳���", "��ʾ", MB_YESNO))
//        {
//            //ȷ���˳�,���ٴ���,�׳�һ��WM_DESTYRY����Ϣ
//            DestroyWindow(hwnd); 
//        }
//        break;
//    case WM_DESTROY:
//        PostQuitMessage(0);
//        break;
//    default:
//        return DefWindowProc(hwnd, uMsg, wParam, lParam);
//    }
//    return 0;
//}
////int WINAPI WinMain (HINSTANCE hInstance,
////					HINSTANCE hPrevInstance,
////					LPSTR szCmdLine,
////					int iCmdShow)
//
//int WINAPI WinMain(HINSTANCE hInstance,      // handle to current instance
//    HINSTANCE hPrevInstance,  // handle to previous instance
//    LPSTR lpCmdLine,          // command line     lpCmdLine
//    int nCmdShow)              // show state
//{
//    //��һ������ƴ�����
//    WNDCLASS wndclass;
//    wndclass.style = CS_HREDRAW | CS_VREDRAW; //����ˮƽ��ֱ�ػ棬����WM_PAINT��Ϣ
//    wndclass.lpfnWndProc = WindowProc; //ָ�����ڵĻص�����
//    wndclass.cbClsExtra = 0;
//    wndclass.cbWndExtra = 0; //������������
//    wndclass.hInstance = hInstance;
//    wndclass.hIcon = LoadIcon(NULL, IDI_APPLICATION);
//    wndclass.hCursor = LoadCursor(NULL, IDC_CROSS);
//    wndclass.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);
//    wndclass.lpszMenuName = NULL;
//    wndclass.lpszClassName = "myWindowClass";
//
//    //�ڶ�����ע�ᴰ����
//    RegisterClass(&wndclass);
//
//	//����������������
//	HWND hWnd;
//	hWnd = CreateWindow(
//		"myWindowClass", //�����������
//		"my first window",//���ڱ���
//		WS_OVERLAPPEDWINDOW,//���ڷ��,��ͨ������ʹ�õ�windows������ʽ
//		450,//ָ�����ڵĳ�ʼˮƽλ��,����Ļ����ϵ�Ĵ��ڵ����Ͻǵ�X����
//		100,//ָ�����ڵĳ�ʼ��ֱλ��,����Ļ����ϵ�Ĵ��ڵ����Ͻǵ�Y����
//		500,//���ڵĿ��
//		500,//���ڵĸ߶�
//		NULL,//�����ھ��
//		NULL,//���ڲ˵����
//		hInstance,//ʵ�����
//		NULL);
//
//    //���Ĳ�����ʾ���´���
//    ShowWindow(hWnd, SW_SHOWNORMAL); //������ʾ����
//    UpdateWindow(hWnd); //���´���
//
//    //���岽����Ϣѭ��
//    MSG msg;
//    while (GetMessageA(&msg, NULL, 0, 0))
//    {
//        TranslateMessage(&msg); //������Ϣ
//        DispatchMessageA(&msg); //����Ϣ���봰�ڵĻص�����
//    }
//	////��Ϣѭ����ʽ2
//	//	MSG msg;
//	//	while(true)
//	//	{
//	//		if(PeekMessage(&msg,NULL,0,0,PM_REMOVE)) //����Ϣ������ȡ��Ϣ
//	//		{
//	//			if(msg.message == WM_QUIT)
//	//				break;
//	//			TranslateMessage (&msg);           //ת����Ϣ
//	//			DispatchMessage (&msg);            //�ɷ���Ϣ
//	//		}
//	//		else
//	//			WaitMessage();
//	//
//	//	} //End of while(true)
//
//
//    return 0;
//}
//
//
//
