
#include <windows.h>

//声明窗口过程函数

LRESULT CALLBACK WndProc(HWND,UINT,WPARAM,LPARAM);

//定义一个全局变量，作为窗口类名

TCHAR szClassName[] = TEXT("SimpleWin32");

//应用程序主函数

int WINAPI WinMain (HINSTANCE hInstance,
					HINSTANCE hPrevInstance,
					LPSTR szCmdLine,
					int iCmdShow)
{

	//窗口类
	WNDCLASS wndclass;

	//当窗口水平方向的宽度和垂直方向的高度变化时重绘整个窗口
	wndclass.style = CS_HREDRAW|CS_VREDRAW;

	//关联窗口过程函数
	wndclass.lpfnWndProc = WndProc;
	wndclass.cbClsExtra = 0;
	wndclass.cbWndExtra = 0;
	wndclass.hInstance = hInstance;//实例句柄
	wndclass.hIcon = LoadIcon(NULL,IDI_APPLICATION);//图标
	wndclass.hCursor = LoadCursor(NULL,IDC_ARROW);//光标
	wndclass.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);//画刷
	wndclass.lpszMenuName  = NULL;//菜单
	wndclass.lpszClassName = szClassName;//类名称

	//注册窗口类
	if(!RegisterClass (&wndclass))
	{
		MessageBox (NULL, TEXT ("RegisterClass Fail!"), 
			szClassName, MB_ICONERROR);
		return 0;
	}



	//建立窗口
	HWND hwnd;
	hwnd = CreateWindow(szClassName,//窗口类名称
	
		TEXT ("窗口测试程序！"),//窗口标题 
		WS_OVERLAPPEDWINDOW,//窗口风格,即通常我们使用的windows窗口样式
		CW_USEDEFAULT,//指定窗口的初始水平位置,即屏幕坐标系的窗口的左上角的X坐标
		CW_USEDEFAULT,//指定窗口的初始垂直位置,即屏幕坐标系的窗口的左上角的Y坐标
		CW_USEDEFAULT,//窗口的宽度
		CW_USEDEFAULT,//窗口的高度
		NULL,//父窗口句柄
		NULL,//窗口菜单句柄
		hInstance,//实例句柄
		NULL);

	ShowWindow(hwnd,iCmdShow);//显示窗口
	UpdateWindow(hwnd);//立即显示窗口

	////消息循环方式1
	//MSG msg;
	//while(GetMessage(&msg,NULL,0,0))//从消息队列中取消息 
	//{
	//	TranslateMessage (&msg);              //转换消息
	//	DispatchMessage (&msg);               //派发消息
	//}
	//return msg.wParam;

	////消息循环方式2
	MSG msg;
	while(true)
	{
		if(PeekMessage(&msg,NULL,0,0,PM_REMOVE)) //从消息队列中取消息
		{
			if(msg.message == WM_QUIT)
				break;
			TranslateMessage (&msg);           //转换消息
			DispatchMessage (&msg);            //派发消息
		}
		else
			WaitMessage();

	} //End of while(true)
}

//消息处理函数

//参数:窗口句柄，消息，消息参数，消息参数

LRESULT CALLBACK WndProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
	//处理感兴趣的消息
	switch (message)
	{
		case WM_CREATE: CreateWindow(TEXT("BUTTON"), //控件"类名称" 
			TEXT("按钮(&A)"), 
			WS_CHILD | WS_VISIBLE |BS_PUSHBUTTON, //控件样式：BS_PUSHBUTTON   BS_DEFPUSHBUTTON   BS_CHECKBOX   BS_AUTOCHECKBOX   BS_RADIOBUTTON   BS_3STATE   BS_AUTO3STATE
			10, 10, 100, 30, hwnd, 
			(HMENU)1000, //控件ID 
			((LPCREATESTRUCT) lParam)->hInstance, //实例句柄 
			NULL); 
		return 0; 

		case WM_DESTROY:
			PostQuitMessage(0);
		return 0;
		
		//当用户关闭窗口，窗口销毁，程序需结束，发退出消息，以退出消息循环
		
	}
	//其他消息交给由系统提供的缺省处理函数
	return ::DefWindowProc (hwnd, message, wParam, lParam);
}

////——————————帅气的分割线—————————– 
//#include <Windows.h>
//
///*
//* 窗口的回调函数
//*/
//LRESULT CALLBACK WindowProc(HWND hwnd,      // handle to window
//    UINT uMsg,      // message identifier
//    WPARAM wParam,  // first message parameter
//    LPARAM lParam)   // second message parameter
//{
//    HDC hDC;
//	PAINTSTRUCT ps;
//
//	//paint中的文本数据
//	char painttest[30]="welcome to yyt6801's virus";
//    switch (uMsg)
//    {
//    case WM_PAINT:
//        /*
//         * 窗口重绘时调用
//         * 只有在WM_PAINT消息中才可以使用BeginPaint、EndPaint
//         * 其他消息使用GetDC、ReleaseDC
//         */
//        hDC = BeginPaint(hwnd, &ps);
//        TextOut(hDC, 0, 50, painttest, strlen(painttest));
//        EndPaint(hwnd, &ps);
//        break;
//    case WM_CHAR:
//        MessageBox(hwnd, "WM_CHAR消息触发了", "提示", MB_OK);
//        break;  
//    case WM_LBUTTONDOWN:
//        hDC = GetDC(hwnd);
//        TextOut(hDC, 0, 70, "onclick", strlen("onclick"));
//        ReleaseDC(hwnd, hDC);
//        break;
//    case WM_CLOSE:
//        if (IDYES == MessageBox(hwnd, "确定要退出吗？", "提示", MB_YESNO))
//        {
//            //确定退出,销毁窗口,抛出一个WM_DESTYRY的消息
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
//    //第一步、设计窗口类
//    WNDCLASS wndclass;
//    wndclass.style = CS_HREDRAW | CS_VREDRAW; //设置水平竖直重绘，发送WM_PAINT消息
//    wndclass.lpfnWndProc = WindowProc; //指定窗口的回调函数
//    wndclass.cbClsExtra = 0;
//    wndclass.cbWndExtra = 0; //两个额外数据
//    wndclass.hInstance = hInstance;
//    wndclass.hIcon = LoadIcon(NULL, IDI_APPLICATION);
//    wndclass.hCursor = LoadCursor(NULL, IDC_CROSS);
//    wndclass.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);
//    wndclass.lpszMenuName = NULL;
//    wndclass.lpszClassName = "myWindowClass";
//
//    //第二步、注册窗口类
//    RegisterClass(&wndclass);
//
//	//第三步、创建窗口
//	HWND hWnd;
//	hWnd = CreateWindow(
//		"myWindowClass", //窗口类的名称
//		"my first window",//窗口标题
//		WS_OVERLAPPEDWINDOW,//窗口风格,即通常我们使用的windows窗口样式
//		450,//指定窗口的初始水平位置,即屏幕坐标系的窗口的左上角的X坐标
//		100,//指定窗口的初始垂直位置,即屏幕坐标系的窗口的左上角的Y坐标
//		500,//窗口的宽度
//		500,//窗口的高度
//		NULL,//父窗口句柄
//		NULL,//窗口菜单句柄
//		hInstance,//实例句柄
//		NULL);
//
//    //第四部、显示更新窗口
//    ShowWindow(hWnd, SW_SHOWNORMAL); //正常显示窗口
//    UpdateWindow(hWnd); //更新窗口
//
//    //第五步、消息循环
//    MSG msg;
//    while (GetMessageA(&msg, NULL, 0, 0))
//    {
//        TranslateMessage(&msg); //翻译消息
//        DispatchMessageA(&msg); //将消息传入窗口的回调函数
//    }
//	////消息循环方式2
//	//	MSG msg;
//	//	while(true)
//	//	{
//	//		if(PeekMessage(&msg,NULL,0,0,PM_REMOVE)) //从消息队列中取消息
//	//		{
//	//			if(msg.message == WM_QUIT)
//	//				break;
//	//			TranslateMessage (&msg);           //转换消息
//	//			DispatchMessage (&msg);            //派发消息
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
