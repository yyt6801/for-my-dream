
#include <windows.h>
#include <winsock2.h>

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
           TEXT ("The Simple Win32 Application"),//���ڱ��� 
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

    //��Ϣѭ��
    MSG msg;
    while(GetMessage(&msg,NULL,0,0))//����Ϣ������ȡ��Ϣ 
    {
           TranslateMessage (&msg);              //ת����Ϣ
           DispatchMessage (&msg);               //�ɷ���Ϣ
    }
    return msg.wParam;
}

//��Ϣ������

//����:���ھ������Ϣ����Ϣ��������Ϣ����

LRESULT CALLBACK WndProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    //�������Ȥ����Ϣ
    switch (message)
    {
    case WM_DESTROY:
           //���û��رմ��ڣ��������٣���������������˳���Ϣ�����˳���Ϣѭ��
           PostQuitMessage(0);
           return 0;
    }
    //������Ϣ������ϵͳ�ṩ��ȱʡ������
    return ::DefWindowProc (hwnd, message, wParam, lParam);
}