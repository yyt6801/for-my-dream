# autoIP.bat
@echo off
cd /d %~dp0
%1 start "" mshta vbscript:createobject("shell.application").shellexecute("""%~0""","::",,"runas",1)(window.close)&exit
netsh interface ip set address name="以太网" source=dhcp
netsh interface ip set address name="WLAN" source=dhcp



# renewIP.bat
ipconfig/flushdns
ipconfig/release
ipconfig/renew
pause


# 设置以太网Ip为10.20.32.247.bat
netsh interface ip set address name=以太网 source=static addr=10.20.32.247 mask=255.255.255.0
pause

# 设置无线网wlan的Ip为_10.20.32.252.bat
netsh interface ip set address name=WLAN source=static addr=10.20.32.252 mask=255.255.255.0
pause



# 修改路由表到192.168.1.1.bat
cd /d %~dp0
%1 start "" mshta vbscript:createobject("shell.application").shellexecute("""%~0""","::",,"runas",1)(window.close)&exit
route add 10.151.18.86 192.168.1.1
route add 10.151.18.218 192.168.1.1
route add 10.151.18.165 192.168.1.1
pause




# oracle开启服务
cd /d %~dp0
%1 start "" mshta vbscript:createobject("shell.application").shellexecute("""%~0""","::",,"runas",1)(window.close)&exit
net start OracleServiceNERCAR
net start OracleOraDb11g_home1TNSListener
pause


# oracle关闭服务
cd /d %~dp0
%1 start "" mshta vbscript:createobject("shell.application").shellexecute("""%~0""","::",,"runas",1)(window.close)&exit
NET STOP OracleServiceNERCAR
NET STOP OracleOraDb11g_home1TNSListener
NET STOP OracleDBConsolenercar
NER STOP Oracl NERCAR VSS Writer Service



# 打开虚拟机Vmware服务及应用.bat
@echo off
cd /d %~dp0
%1 start "" mshta vbscript:createobject("shell.application").shellexecute("""%~0""","::",,"runas",1)(window.close)&exit
net start "VMware Authorization Service"
net start "VMware DHCP Service"
net start "VMware NAT Service"
net start "VMware USB Arbitration Service"
net start "VMware Workstation Server"
start "" "F:\vmware\vmware.exe"
exit