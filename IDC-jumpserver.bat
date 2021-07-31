REM 这样不会阻塞终端，好像是直接ssh.exe进程，不是附着于cmd里的进程
cmd /c start ssh -L 127.0.0.1:9090:10.0.0.148:80 zhanglikun@58.215.161.74
cmd /c start http://127.0.0.1:9090/luna/
