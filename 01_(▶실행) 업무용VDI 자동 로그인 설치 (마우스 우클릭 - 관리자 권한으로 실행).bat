reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\kt.com\ktvdi" /v "https" /t REG_DWORD /d "2" /f
reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\Zones\2" /v "1A00" /t REG_DWORD /d "0" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Edge\AutoOpenFileTypes" /v "10" /t REG_SZ /d "ica" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Google\Chrome\AutoOpenFileTypes" /v "10" /t REG_SZ /d "ica" /f
timeout /t 2

cd /d %~dp0\Install Files
CitrixWorkspaceAppWeb.exe /includeSSON
url_redirection_pc.exe
timeout /t 3

copy "C:\Program Files (x86)\Citrix\ICA Client\Configuration\receiver.admx" "C:\Windows\PolicyDefinitions\receiver.admx" /Y
copy "C:\Program Files (x86)\Citrix\ICA Client\Configuration\CitrixBase.admx" "C:\Windows\PolicyDefinitions\CitrixBase.admx" /Y
copy "C:\Program Files (x86)\Citrix\ICA Client\Configuration\ko-KR\receiver.adml" "C:\Windows\PolicyDefinitions\ko-KR\receiver.adml" /Y
copy "C:\Program Files (x86)\Citrix\ICA Client\Configuration\ko-KR\CitrixBase.adml" "C:\Windows\PolicyDefinitions\ko-KR\CitrixBase.adml" /Y
timeout /t 2

copy "KT VDI Auto Login s.exe" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\KT VDI Auto Login s.exe" /Y
copy "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Pulse Secure\Pulse Secure.lnk" "C:\Users\Public\Desktop\Pulse Secure.lnk" /Y
copy "KT VDI.ico"  "C:\Program Files (x86)\Citrix\KT VDI.ico" /Y
copy "KT VDI 자동로그인.url" "%UserProfile%\Desktop\KT VDI 자동로그인.url" /Y
timeout /t 2

gpupdate /force

@echo off
net stop CWAUpdaterService
sc config "CWAUpdaterService" start= disabled 

@echo off
echo.
echo.
echo.
echo 수고하셨습니다. 로컬PC를 재부팅 해주세요!!!
echo.
echo.

timeout /t 3