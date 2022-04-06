import pyotp
import subprocess
import configparser

config=configparser.ConfigParser()
config.read('config.ini')

totp = pyotp.TOTP(config['secret']['totp_seed'])               # 这里要填写的totp的seed，一般解析一下二维码就能获得
password = config['secret']['password'] + totp.now()           # 固定密码


with open(r"C:\Users\iuxt\OpenVPN\config\password.txt", "w") as f:   # 这里是password.txt文件位置
    f.write("%s\n%s" % (config['secret']['username'], password))
    
subprocess.run([r"C:\Program Files\OpenVPN\bin\openvpn.exe", r"C:\Users\iuxt\OpenVPN\config\win.ovpn"])  # vpn可执行位置和vpn配置文件位置

