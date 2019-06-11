
#include <windows.h>
#include <winsock2.h>

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
           TEXT ("The Simple Win32 Application"),//窗口标题 
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

    //消息循环
    MSG msg;
    while(GetMessage(&msg,NULL,0,0))//从消息队列中取消息 
    {
           TranslateMessage (&msg);              //转换消息
           DispatchMessage (&msg);               //派发消息
    }
    return msg.wParam;
}

//消息处理函数

//参数:窗口句柄，消息，消息参数，消息参数

LRESULT CALLBACK WndProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    //处理感兴趣的消息
    switch (message)
    {
    case WM_DESTROY:
           //当用户关闭窗口，窗口销毁，程序需结束，发退出消息，以退出消息循环
           PostQuitMessage(0);
           return 0;
    }
    //其他消息交给由系统提供的缺省处理函数
    return ::DefWindowProc (hwnd, message, wParam, lParam);
}