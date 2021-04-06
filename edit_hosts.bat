@echo off
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit

cd "C:\Program Files\Notepad++"
start notepad++.exe C:\Windows\System32\drivers\etc\hosts
REM start C:\Progra~1\Notepad++\notepad++.exe C:\Windows\System32\drivers\etc\hosts
