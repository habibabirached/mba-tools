
# One time install modules. Don't need to do it after that.
# Can be commented out.

Install-Module PSWindowsUpdate
Add-WUServiceManager -MicrosoftUpdate

# This is to install the updates. Will be needed each time.

Install -WindowsUpdate -MicrosoftUpdate -AcceptAll -AutoReboot

Timeout /T 10

# For the Office updates

cd 'C:\Program Files\Common Files\microsoft shared\ClickToRun\'
./Office2RClient.exe /update user


