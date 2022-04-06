import pyotp
import os
 
totp = pyotp.TOTP('YKHINPAIJL42CDABI354SRELNTL22XVP')
totp_password = totp.now()
 
def addToClipBoard(text):
    command = 'echo|set /p= ' + text.strip() + '| clip'
    os.system(command)
 
addToClipBoard("WOSHIgty123" + totp_password)