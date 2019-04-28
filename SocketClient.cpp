// Client.cpp : Defines the entry point for the console application.
//�ͻ��˳����� 
//1.��ʼ�� Winsock�� 
//2.����ͨ���׽���(socket()����) 
//3.��дҪ���ӵķ������ĵ�ַ�ṹ 
//4.���������������(connect()����) 
//5.����recv()�������շ���������,send()�����������ݸ�������

#include "stdafx.h"
#include <iostream>
#include <WinSock2.h>
using namespace std;

#pragma comment(lib, "WS2_32.lib")
//��ʾ����WS2_32.lib����⡣
//#define  PORT 12306

int main()
{
    SOCKET sock_client;
    struct sockaddr_in server_addr;
    int addr_len = sizeof(struct sockaddr_in);
    char msgbuffer[1000];
    memset(msgbuffer, 0, sizeof(msgbuffer));
    // ��ʼ�� winsock2.dll[12/27/2017 MagicScaring]
    WSADATA wsaData;
    WORD wVersionRequested = MAKEWORD(2, 2);        //���ɰ汾��
    if (WSAStartup(wVersionRequested, &wsaData) != 0)
    {
        cout << "���� winsock.dllʧ��" << endl;
        return 0;
    }
    // �����׽��� [12/27/2017 MagicScaring]
    if ((sock_client = socket(AF_INET, SOCK_STREAM, 0)) == SOCKET_ERROR)
    {
        cout << "�����׽���ʧ��! �������:" << WSAGetLastError() << endl;
        WSACleanup();                   //ע��WinSock��̬���ӿ�
        return 0;
    }
    // ��д��������ַ [12/27/2017 MagicScaring]
    //char IP[20] = { "192.168.5.38" };
    char IP[20];
    cout << "�����������ַ:" << endl;
    cin >> IP;
	int PORT=0;
	cout << "����˿ں�:" << endl;
	cin >> PORT;
    memset((void*)&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = inet_addr(IP);

    // ��������������� [12/27/2017 MagicScaring]
   if (connect(sock_client, (struct sockaddr*)&server_addr, addr_len) == SOCKET_ERROR)
    {
        cout << "����ʧ��! �������:" << WSAGetLastError() << endl;
        closesocket(sock_client);
        WSACleanup();
        return 0;
    }
    while (true)
    {
        int sizes;
        if ((sizes = recv(sock_client, msgbuffer, sizeof(msgbuffer), 0)) == SOCKET_ERROR)
        {
            cout << "������Ϣʧ�ܣ� ������룺" << WSAGetLastError() << endl;
            closesocket(sock_client);
            WSACleanup();
            return 0;
        }
        else if (sizes == 0)
        {
            cout << "�Է��ѹر�����" << endl;
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
		cout << "���뷢������:" << endl;
		cin >> send_msg;
		if((sizes = send(sock_client, send_msg, sizeof(send_msg),0)) == SOCKET_ERROR)
        {
            cout << "������Ϣʧ��! �������:" << WSAGetLastError() << endl;
        }
        else if (sizes == 0)
        {
            cout << "�Է��ѹر�����" << endl;
        }
        else
        {
            cout << "��Ϣ���ͳɹ�" << endl;
			sizes=0;
        }
		}
    }
    closesocket(sock_client);
    WSACleanup();

    return 0;
}