# Go to Directory containing python scripts
cd "C:\Users\200016890\Desktop\BackgroundInfo" # remove my SSO and replace with correct location

# Execute Python Script(s) - Comment out (#) what you don't need
.\BackgroundInformationSheet.py 
.\HealthQuestionnaire.py
.\SelfAssessment.py
.\testFileWrite.py

# Pause to let Python instances launch
start-sleep -seconds 2

# Open Edge browser to specified pages  -- Comment out what you don't need
start shell:AppsFolder\Microsoft.MicrosoftEdge_8wekyb3d8bbwe!MicrosoftEdge http://127.0.0.1:5000/BISform   
start shell:AppsFolder\Microsoft.MicrosoftEdge_8wekyb3d8bbwe!MicrosoftEdge http://127.0.0.1:5001/HQform
start shell:AppsFolder\Microsoft.MicrosoftEdge_8wekyb3d8bbwe!MicrosoftEdge http://127.0.0.1:5002/SAform
start shell:AppsFolder\Microsoft.MicrosoftEdge_8wekyb3d8bbwe!MicrosoftEdge http://127.0.0.1:5400/test           #I don't remember the full address for this one 

# Open Test Software
start-process -filepath "C:\Program Files (x86)\MAB\MAB.EXE" -window maximized  

# Add paths of other test software packages

# Open (minimized) file explorer window for NEO-PI (if runing, otherwise comment out)
cd 'C:\path to client files' # replace with correct directory
start . -window minimized