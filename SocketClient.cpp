// Client.cpp : Defines the entry point for the console application.
//客户端程序工作 
//1.初始化 Winsock库 
//2.创建通信套接字(socket()函数) 
//3.填写要连接的服务器的地址结构 
//4.与服务器建立连接(connect()函数) 
//5.调用recv()函数接收服务器数据,send()函数发送数据给服务器

#include "stdafx.h"
#include <iostream>
#include <WinSock2.h>
using namespace std;

#pragma comment(lib, "WS2_32.lib")
//表示链接WS2_32.lib这个库。
//#define  PORT 12306

int main()
{
    SOCKET sock_client;
    struct sockaddr_in server_addr;
    int addr_len = sizeof(struct sockaddr_in);
    char msgbuffer[1000];
    memset(msgbuffer, 0, sizeof(msgbuffer));
    // 初始化 winsock2.dll[12/27/2017 MagicScaring]
    WSADATA wsaData;
    WORD wVersionRequested = MAKEWORD(2, 2);        //生成版本号
    if (WSAStartup(wVersionRequested, &wsaData) != 0)
    {
        cout << "加载 winsock.dll失败" << endl;
        return 0;
    }
    // 创建套接字 [12/27/2017 MagicScaring]
    if ((sock_client = socket(AF_INET, SOCK_STREAM, 0)) == SOCKET_ERROR)
    {
        cout << "创建套接字失败! 错误代码:" << WSAGetLastError() << endl;
        WSACleanup();                   //注销WinSock动态链接库
        return 0;
    }
    // 填写服务器地址 [12/27/2017 MagicScaring]
    //char IP[20] = { "192.168.5.38" };
    char IP[20];
    cout << "输入服务器地址:" << endl;
    cin >> IP;
	int PORT=0;
	cout << "输入端口号:" << endl;
	cin >> PORT;
    memset((void*)&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = inet_addr(IP);

    // 与服务器建立连接 [12/27/2017 MagicScaring]
   if (connect(sock_client, (struct sockaddr*)&server_addr, addr_len) == SOCKET_ERROR)
    {
        cout << "连接失败! 错误代码:" << WSAGetLastError() << endl;
        closesocket(sock_client);
        WSACleanup();
        return 0;
    }
    while (true)
    {
        int sizes;
        if ((sizes = recv(sock_client, msgbuffer, sizeof(msgbuffer), 0)) == SOCKET_ERROR)
        {
            cout << "接收信息失败！ 错误代码：" << WSAGetLastError() << endl;
            closesocket(sock_client);
            WSACleanup();
            return 0;
        }
        else if (sizes == 0)
        {
            cout << "对方已关闭连接" << endl;
            closesocket(sock_client);
            WSACleanup();
            return 0;
        }
        else
        {
            cout << "The message from Server:" << msgbuffer << endl;
        }
		while(1)
		{
        //char send_msg[1000] = { "Hello server" };
		char send_msg[1000];
		cout << "输入发送内容:" << endl;
		cin >> send_msg;
		if((sizes = send(sock_client, send_msg, sizeof(send_msg),0)) == SOCKET_ERROR)
        {
            cout << "发送信息失败! 错误代码:" << WSAGetLastError() << endl;
        }
        else if (sizes == 0)
        {
            cout << "对方已关闭连接" << endl;
        }
        else
        {
            cout << "信息发送成功" << endl;
			sizes=0;
        }
		}
    }
    closesocket(sock_client);
    WSACleanup();

    return 0;
}