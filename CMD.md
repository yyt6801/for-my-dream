@echo off
cd /d %~dp0
%1 start "" mshta vbscript:createobject("shell.application").shellexecute("""%~0""","::",,"runas",1)(window.close)&exit
netsh interface ip set address name="以太网" source=dhcp
netsh interface ip set address name="WLAN" source=dhcp