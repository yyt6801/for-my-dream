import sys
import os

#得到要发送的数据信息
def getHtmlFile(data):
    msgSendtoClient=""
    requestType=data[0:data.find("/")].rstrip()
    #判断是GET请求还是POST请求
    if requestType=="GET":
        msgSendtoClient=responseGetRequest(data,msgSendtoClient)
    if requestType=="POST":
        msgSendtoClient=responsePostRequest(data,msgSendtoClient)
    return msgSendtoClient

#打开文件，这里不直接写，二是去取要发送的文件再写
def getFile(msgSendtoClient,file):
        for line in file:
          msgSendtoClient+=line
        return msgSendtoClient

#筛选出请求的一个方法
def getMidStr(data,startStr,endStr):
    startIndex = data.index(startStr)
    if startIndex>=0:
        startIndex += len(startStr)
        endIndex = data.index(endStr)
        return data[startIndex:endIndex]

#获取要发送数据的大小，根据HTTP协议规范，要提前指定发送的实体内容的大小
def getFileSize(fileobject):
    fileobject.seek(0,2)
    size = fileobject.tell()
    return size

#设置编码格式和文件类型
def setParaAndContext(msgSendtoClient,type,file,openFileType):
    msgSendtoClient+="Content-Type: "+type+";charset=utf-8"
    msgSendtoClient+="Content-Length: "+str(getFileSize(open(file,"r")))+"\n"+"\n"
    htmlFile=open(file,openFileType)
    msgSendtoClient=getFile(msgSendtoClient,htmlFile)
    return msgSendtoClient

#GET请求的返回数据
def responseGetRequest(data,msgSendtoClient):
    return responseRequest(getMidStr(data,'GET /','HTTP/1.1'),msgSendtoClient)

#POST请求的返回数据
def responsePostRequest(data,msgSendtoClient):
    return responseRequest(getMidStr(data,'POST /','HTTP/1.1'),msgSendtoClient)

#请求返回数据
def responseRequest(getRequestPath,msgSendtoClient):
    headFile=open("head.txt","r")
    msgSendtoClient=getFile(msgSendtoClient,headFile)
    if getRequestPath==" ":
        msgSendtoClient=setParaAndContext(msgSendtoClient,"text/html","index.html","r")
    else:
        rootPath=getRequestPath
        if os.path.exists(rootPath) and os.path.isfile(rootPath):
            if ".html" in rootPath:
                msgSendtoClient=setParaAndContext(msgSendtoClient,"text/html",rootPath,"r")
            if ".css" in rootPath:
                msgSendtoClient=setParaAndContext(msgSendtoClient,"text/css",rootPath,"r")
            if ".js" in rootPath:
                msgSendtoClient=setParaAndContext(msgSendtoClient,"application/x-javascript",rootPath,"r")
            if ".gif" in rootPath:
                msgSendtoClient=setParaAndContext(msgSendtoClient,"image/gif",rootPath,"rb")
            if ".doc" in rootPath:
                msgSendtoClient=setParaAndContext(msgSendtoClient,"application/msword",rootPath,"rb")
            if ".mp4" in rootPath:
                msgSendtoClient=setParaAndContext(msgSendtoClient,"video/mpeg4",rootPath,"rb")
        else:
            msgSendtoClient=setParaAndContext(msgSendtoClient,"application/x-javascript","file.js","r")
    return msgSendtoClient