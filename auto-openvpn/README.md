openvpn安装在默认位置

将所有文件拷贝到配置文件目录C:\Users\iuxt\OpenVPN\config

复制config.ini.example到config.ini修改里面的选项

win.ovpn需要修改`auth-user-pass C:\\Users\\iuxt\\OpenVPN\\config\\password.txt`需要和start.py里面路径保持一致

双击start.bat即可自动连接

ctrl + c 即可关闭

如果有隐藏cmd窗口的需求，可以看看这篇<https://zahui.fan/3b6d9935/>