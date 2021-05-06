@echo off

choice /t 20 /d y /n >nul

setlocal enabledelayedexpansion
for /f "delims=" %%i in ('type "config.ini"^| find /i "="') do set %%i
echo %url%
echo %username%

REM 映射到Z盘, PERSISTENT表示是否记忆
net use Z: %url% /user:%username% %password% /PERSISTENT:no

REM 这个是将一个目录映射成一个盘, 不过有些软件不兼容.
REM subst D: C:\Files

