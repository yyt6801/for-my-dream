// testsomething.cpp : Defines the entry point for the console application.
//

//Server.cpp : Defines the entry point for the console application.
//������������ 
//1.��ʼ�� Winsock�� 
//2.���������׽���(socket()����) 
//3.��дҪ�󶨵ı��ص�ַ�ṹ(bind()����) 
//4.�������׽��ְ󶨱���IP��ַ 
//5.��ʼ����(listen()����) 
//6.ѭ��ִ�� ����accept()�������տͻ�����������,���accept()�������سɹ�.�����send()������ͻ��˷������ݻ��ߵ���recv()�����ӿͻ��˽�������

#include <iostream>
#include <WinSock2.h>
#include <string.h>
using namespace std;

#pragma comment(lib, "WS2_32.lib")
//��ʾ����WS2_32.lib����⡣
//#define  PORT 1024

int main()
{
	SOCKET sock_server, newsock;
	struct sockaddr_in server_addr, client_addr; 
	char msg[] = { "Hello clinet\0" };
	// ��ʼ�� winsock2.dll[12/27/2017 MagicScaring]
	WSADATA wsaData;
	WORD wVersionRequested = MAKEWORD(2, 2);        //���ɰ汾��
	if (WSAStartup(wVersionRequested, &wsaData) != 0)
	{
		cout << "���� winsock.dllʧ��" << endl;
		return 0;
	}
	// �����׽��� [12/27/2017 MagicScaring]
	if ((sock_server = socket(AF_INET, SOCK_STREAM, 0)) == SOCKET_ERROR)
	{
		cout << "�����׽���ʧ��! �������:" << WSAGetLastError() << endl;
		WSACleanup();                   //ע��WinSock��̬���ӿ�
		return 0;
	}
	// ��д��Ҫ�󶨵ı��ص�ַ [12/27/2017 MagicScaring]
	int addr_len = sizeof(struct sockaddr_in);
	memset((void*)&server_addr, 0, sizeof(server_addr));
	server_addr.sin_family = AF_INET;
	int PORT=0;
	cout << "����Ҫ�򿪵Ķ˿�:" << endl;
	cin >> PORT;
	server_addr.sin_port = htons(PORT);
	server_addr.sin_addr.s_addr = htonl(INADDR_ANY);

	if (bind(sock_server, (struct sockaddr*)&server_addr, addr_len) != 0)
	{
		cout << "��ʧ��!�������:" << WSAGetLastError() << endl;
		closesocket(sock_server);               //�ر��������׽���
		WSACleanup();                           //ע��WinSock��̬���ӿ�
		return 0;
	}

	// ��ʼ���� [12/27/2017 MagicScaring]
	if (listen(sock_server, 0) != 0)
	{
		cout << "listen����ʧ��!�������:" << WSAGetLastError() << endl;
		closesocket(sock_server);
		WSACleanup();
		return 0;
	}
	else
	{
		cout << "listening...." << endl;
	}
	// ѭ��:�������������շ����� [12/27/2017 MagicScaring]
	int size;
	char msgrec[64];
	while (true)
	{
		if ((newsock = accept(sock_server, (struct sockaddr *)&client_addr, &addr_len)) == INVALID_SOCKET)
		{
			cout << "accept ��������ʧ��! �������:" << WSAGetLastError() << endl;
			break;
		}
		else
		{
			cout << "�ɹ����յ�һ����������!" << endl;
		while(1){
			char msg[1000];
			cout << "����Ҫ��������:" << endl;
			cin >> msg;
			
			size = send(newsock, msg, sizeof(msg), 0);
			if (size == SOCKET_ERROR)
			{
				cout << "������Ϣʧ��! �������:" << WSAGetLastError() << endl;
				closesocket(newsock);
				continue;
			}
			else if (size == 0)
			{
				cout << "�Է��ѹر�����" << endl;
				closesocket(newsock);
				continue;
			}
			else
			{
				cout << "��Ϣ���ͳɹ�" << endl;
			}
		}
			while(1)
			{
				//memset(msgrec,0x00,sizeof(msgrec));
				//strcat(msg,"000");
				size = recv(newsock, msgrec, sizeof(msgrec), 0);
				//strcat(msg,"\0");
				//cout<<'123'<<size<<endl;
				if (size == SOCKET_ERROR)
				{
					cout << "������Ϣʧ�ܣ� ������룺" << WSAGetLastError() << endl;
					closesocket(newsock);
					WSACleanup();
					return 0;
				}
				else if (size == 0)
				{
					cout << "�Է��ѹر�����" << endl;
					closesocket(newsock);
					WSACleanup();
					return 0;
				}
				else if(msgrec[0]>=48 && msgrec[0]<=57)
				{
					cout << "The message from Client:" << msgrec << endl;
					//��Ӻ���
				}
			}

		}

	}

	return 0;
}
