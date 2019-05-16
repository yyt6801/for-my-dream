// Module Name: Client.c
//
// Description:
//    This sample is the echo client. It connects to the TCP server,
//    sends data, and reads data back from the server. 
//
// Compile:
//    cl -o Client Client.c ws2_32.lib
//
// Command Line Options:
//    client [-p:x] [-s:IP] [-n:x] [-o]
//           -p:x      Remote port to send to
//           -s:IP     Server's IP address or hostname
//           -n:x      Number of times to send message
//           -o        Send messages only; don't receive
//  
#include <winsock2.h>
#include <stdio.h>
#include <stdlib.h>

#define DEFAULT_COUNT       20
#define DEFAULT_PORT        5150
#define DEFAULT_BUFFER      2048
#define DEFAULT_MESSAGE     "This is a test of the emergency \
broadcasting system"

char  szServer[128],          // Server to connect to
      szMessage[1024];        // Message to send to sever
int   iPort     = DEFAULT_PORT;  // Port on server to connect to
DWORD dwCount   = DEFAULT_COUNT; // Number of times to send message
BOOL  bSendOnly = FALSE;         // Send data only; don't receive

//
// Function: usage:
//
// Description:
//    Print usage information and exit
//
void usage()
{
    printf("usage: client [-p:x] [-s:IP] [-n:x] [-o]\n\n");
    printf("       -p:x      Remote port to send to\n");
    printf("       -s:IP     Server's IP address or hostname\n");
    printf("       -n:x      Number of times to send message\n");
    printf("       -o        Send messages only; don't receive\n");
    ExitProcess(1);
}

//
// Function: ValidateArgs
//
// Description:
//    Parse the command line arguments, and set some global flags 
//    to indicate what actions to perform
//
void ValidateArgs(int argc, char **argv)
{
    int                i;

    for(i = 1; i < argc; i++)
    {
        if ((argv[i][0] == '-') || (argv[i][0] == '/'))
        {
            switch (tolower(argv[i][1]))
            {
                case 'p':        // Remote port
                    if (strlen(argv[i]) > 3)
                        iPort = atoi(&argv[i][3]);
                    break;
                case 's':       // Server
                    if (strlen(argv[i]) > 3)
                        strcpy(szServer, &argv[i][3]);
                    break;
                case 'n':       // Number of times to send message
                    if (strlen(argv[i]) > 3)
                        dwCount = atol(&argv[i][3]);
                    break;
                case 'o':       // Only send message; don't receive
                    bSendOnly = TRUE;
                    break;
                default:
                    usage();
                    break;
            }
        }
    }
}

// 
// Function: main
//
// Description:
//    Main thread of execution. Initialize Winsock, parse the 
//    command line arguments, create a socket, connect to the 
//    server, and then send and receive data.
//
int main(int argc, char **argv)
{
    WSADATA       wsd;
    SOCKET        sClient;
    char          szBuffer[DEFAULT_BUFFER];
    int           ret,
                  i;
    struct sockaddr_in server;
	struct sockaddr_in		srv_addr;
    struct hostent    *host = NULL;
	struct linger           ling;

	char t1;
	char t2[2]="a";

	strncpy(&t1, t2,1);




	
    // Parse the command line and load Winsock
    //
//    ValidateArgs(argc, argv);
    if (WSAStartup(MAKEWORD(2,2), &wsd) != 0)
    {
        printf("Failed to load Winsock library!\n");
        return 1;
    }
//    strcpy(szMessage, DEFAULT_MESSAGE);
    //
    // Create the socket, and attempt to connect to the server
    //
    sClient = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (sClient == INVALID_SOCKET)
    {
        printf("socket() failed: %d\n", WSAGetLastError());
        return 1;
    }


	(void)memset(&srv_addr,0X00,sizeof(srv_addr));
	srv_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
	srv_addr.sin_family=AF_INET;
	srv_addr.sin_port= htons (1200);
	if (bind(sClient,(LPSOCKADDR)&srv_addr,sizeof(srv_addr))==SOCKET_ERROR)
	{
        printf("bind() failed: %d\n", WSAGetLastError());
        return 1;
	}

	
    server.sin_family = AF_INET;
    server.sin_port = htons(1100);
    server.sin_addr.s_addr = inet_addr("127.0.0.1");
    //
    // If the supplied server address wasn't in the form
    // "aaa.bbb.ccc.ddd" it's a hostname, so try to resolve it
    //
    if (server.sin_addr.s_addr == INADDR_NONE)
    {
        host = gethostbyname(szServer);
        if (host == NULL)
        {
            printf("Unable to resolve server: %s\n", szServer);
			WSACleanup();
			return 1;
        }
        CopyMemory(&server.sin_addr, host->h_addr_list[0],
            host->h_length);
    }
    if (connect(sClient, (struct sockaddr *)&server, 
        sizeof(server)) == SOCKET_ERROR)
    {
        printf("connect() failed: %d\n", WSAGetLastError());
		WSACleanup();
		return 1;
    }
    // Send and receive data 
    //
//    for(i = 0; i < dwCount; i++)
//    {
            ret = recv(sClient, szBuffer, DEFAULT_BUFFER, 0);
            szBuffer[ret] = '\0';
            printf("RECV [%d bytes]: '%s'\n", ret, szBuffer);
//    }
	ling.l_onoff = 1;
	ling.l_linger = 0;
	ret=setsockopt(sClient, SOL_SOCKET, SO_LINGER,(char *)&ling, sizeof(struct linger));
	getchar();
	ret=shutdown(sClient,SD_SEND);
    ret=closesocket(sClient);
	Sleep(100);

    WSACleanup();
    return 0;
}
