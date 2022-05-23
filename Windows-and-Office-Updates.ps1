
# One time install modules. Don't need to do it after that.

Install-Module PSWindowsUpdate
Add-WUServiceManager -MicrosoftUpdate

Install -WindowsUpdate -MicrosoftUpdate -AcceptAll -AutoReboot

Timeout /T 10

cd 'C:\Program Files\Common Files\microsoft shared\ClickToRun\'
./Office2RClient.exe /update user


