$pathParent = 'C:\PATH TO WHATEVER YOU WANT'   # <-- Change this to the path to where some set of files are
$dirDest = 'MAB_Files'                                  # <-- Change this to the directory you want the files copied to on the USB drive
$filetype = '*.mab'   #mab'                                  # <-- Change this to the file type of interest

# Determine Drive letter of USB 
$usbPath = $MyInvocation.MyCommand.Path
$usbRoot = Split-Path $usbPath -Parent
write-output "All files will copy to: $usbRoot$dirDest"

# check for Destination directory exists and make if needed
function Create-Dir($path)
{
  if(! (Test-Path $path))
  {
    Write-Host "Creating: $path"
    New-Item -Path $path -ItemType Directory
  }
  else
  {
    Write-Host "Path $path already exists"
  }
}

function CopyToUSB($usbRoot, $path, $dirDest, $filetype)
    {
        write-host "$path is the path"
        if(Test-Path $path)    # Tests that the path in question exists
            {
                Write-Host "Source File Path ($path) exists"
                cd $path
                $filz = Get-ChildItem -Path $path -Filter $filetype -Recurse -ErrorAction SilentlyContinue -Force       # Find files of filetype in directories within path
                $filcount = ($filz.Name).Count                                                                          # Count how many files found
                Write-Host "$filcount $filetype files found"
                if($filcount -ge 1)
                    {
                        write-host "$filcount $filetype files found"
                        for($nn = 0; $nn -le ($filcount - 1); $nn++) 
                            {
                                write-host "$nn" 
                                $dirName = $filz[$nn].Directory.Name
                                $filName = $filz[$nn].Name
                              #  move-item "$path\$dirName\$filName" "$usbRoot$dirDest\$filName"       # <-- Comment out this line to switch to copy 
                                copy-item "$path\$dirName\$filName" "$usbRoot$dirDest\$filName"      # <-- Un-comment this line to copy rather than move
                                write-host "Copying $filName"
                            }
                    }
                else
                    {
                        write-host "No $filetype files found"
                    }
            }
    }

Create-Dir($usbRoot+$dirDest)        # Check existence / make USB drive directory
CopyToUSB -usbRoot $usbRoot -path $pathParent -dirDest $dirDest -filetype $filetype           # Do the thing. 