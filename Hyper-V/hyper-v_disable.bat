@echo off
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"

pushd "%~dp0"
dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum >hyper-v.txt
for /f %%i in ('findstr /i . hyper-v.txt 2^>nul') do dism /online /norestart /Remove-Package:"%SystemRoot%\servicing\Packages\%%i"
del hyper-v.txt
Dism /online /disable-feature /featurename:Microsoft-Hyper-V-All /LimitAccess /ALL

bcdedit /set hypervisorlaunchtype off