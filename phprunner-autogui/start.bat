rd /s /q %USERPROFILE%\\Downloads\\output

set app=hg-forum-39966

.\venv\scripts\python.exe autogui.py %app%

if %app% == hg-fapiao-17920 (
    set oauth_script=runner-jianguoyun-oauth.sh
) else if %app% == hg-forum-39966 (
    set oauth_script=runner-forum_ws.sh
) else if %app% == hg-hetong-20489 (
    set oauth_script=runner-jianguoyun-oauth.sh
)


wsl -d Ubuntu sudo service docker start
wsl -d Ubuntu bash -c "cd ~/code/nutstore-huige/hgprod_with_oauth/ && rm -rf output"
wsl -d Ubuntu mv /mnt/c/Users/iuxt/Downloads/output/ ~/code/nutstore-huige/hgprod_with_oauth/
wsl -d Ubuntu bash -c "cd ~/code/nutstore-huige/hgprod_with_oauth/ && export PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/go/bin && ./%oauth_script% && ./deploy.sh"

rd /s /q %USERPROFILE%\\Downloads\\input
rd /s /q %USERPROFILE%\\Downloads\\output
pause