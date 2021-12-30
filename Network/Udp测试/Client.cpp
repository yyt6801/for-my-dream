/*
* Copyright (c) 2004, NERCAR
* All rights reserved.
* 
* 文件名称：Recognition.cpp
* 摘    要：UDP通信代码（拷贝至对方程序）
* 
* 版本历史：
*     2019-05-29    v1.0     LiLiGang    创建   
*/

#include <winsock.h>
#include <stdlib.h>
#include <stdio.h>
#include <tchar.h>
#include <winsock.h>
#include <string.h>

// 电文头
typedef struct _TEL_HEAD
{
	short ID;												//Telegram ID
	short Len;											//Length of Telegram
	short Counter;									    //1~9999
	short Flag;

}TEL_HEAD,*LPTEL_HEAD;

// 发送电文
// ID=6002  length = 296
typedef struct _Idetify
{
	TEL_HEAD		head;								//Telegram Head
    int             group; 
	float           set;
    float           act;
	float           qact;
	char            spare[1002];
}IDENTIFY,*LPIDENTIFY;

/*
*	主程序
*/
int  _tmain(int argc, _TCHAR* argv[])
{
	WSADATA						WSAData;
	WORD						wd;
	SOCKET						ClientSock = INVALID_SOCKET;
	struct	sockaddr_in			locAddr; 
	struct	sockaddr_in			srvAddr;
	char                        sendBuff[1025];

	//set server socket address	定义目的IPAddr和目的PORT
	(void)memset(&srvAddr,0X00,sizeof(srvAddr));
	srvAddr.sin_addr.s_addr = inet_addr("192.168.67.1");
	if (srvAddr.sin_addr.s_addr == INADDR_NONE)
	{
		printf("couldn't set server socket address	\n");    
		return -1;		
	}
	srvAddr.sin_family = AF_INET;
	srvAddr.sin_port = htons ((unsigned short)12001);
	ZeroMemory(&(srvAddr.sin_zero),8);


	//Initial Windows Socket		
	wd = MAKEWORD(1,1);					  // Socket Version 
	if (WSAStartup(wd, &WSAData) != 0)    //Socket Initial 
	{
		printf("couldn't find a useable winsock.dll\n");    
		return -1;		
	}

	if ( LOBYTE( WSAData.wVersion ) != 1 ||
		HIBYTE( WSAData.wVersion ) != 1 ) 
	{
		printf("couldn't find a useable winsock.dll\n");                            
		WSACleanup( );
		return  -1;
	}

	printf("\n  The Windows Sockets DLL is acceptable\n"); 

	//create socket to connect server		
	ClientSock = socket(AF_INET, SOCK_DGRAM, 0);
	if ( ClientSock == INVALID_SOCKET )
	{
		printf("couldn't create client socket\n");                            
		WSACleanup( );
		return  -1;
	}	

	IDENTIFY		tel_identify;
    int             iCntIdent = 0;
	while ( TRUE )
	{
			memset( sendBuff, 0x00, sizeof( sendBuff ) );

			//发送内容
			memset( &tel_identify, 0x00, sizeof( tel_identify ) );
			tel_identify.head.ID = 12001;//EDH根据ID来解析到对应的电文中
			tel_identify.head.Len= 1024;//ID和长度不算在长度里，会被识别成协议标志头（在通道中设置ID和长度的偏移量，然后从计数器开始算作data）
			iCntIdent = ( ++iCntIdent ) % 9999;
			if ( !iCntIdent ) iCntIdent = 1;
			tel_identify.head.Counter = iCntIdent;
			tel_identify.head.Flag = 1;
			tel_identify.group = 2;
			tel_identify.set = 2110.9;
			tel_identify.act = 220.9;
			tel_identify.qact = 3320.9;
			//尝试把结构体用一整串表示出来
			

			memset( sendBuff, 0x00, sizeof( sendBuff ) );
			memcpy( sendBuff, &tel_identify, tel_identify.head.Len );
			// 发送电文
			if ( sendto( ClientSock, sendBuff, 1024, 0,(struct sockaddr *)&srvAddr, sizeof(sockaddr)) == SOCKET_ERROR)	//send error
			{
				shutdown(ClientSock,2 ); 
				closesocket(ClientSock);
				ClientSock = INVALID_SOCKET;
				printf("SendToServer: select failed \n");                            
				WSACleanup( );
				return  -1;
			}
			else
			{
				printf("SendToServer: select succed \n");  
				memset( &tel_identify, 0x00, sizeof( tel_identify ) );
				memset( sendBuff, 0x00, sizeof( sendBuff ) );

			}
		    Sleep(1000);
	}
	closesocket(ClientSock);                     
	WSACleanup( );
	return  0;

}


