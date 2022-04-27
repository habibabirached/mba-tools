from striprtf.striprtf import rtf_to_text
rtf = "some rtf encoded string"

skip_flag = 0

#with open('PAI_Plus_Score_Report.RTF') as inFile:
with open('PAI.RTF') as inFile:
    for line in inFile:
        line = line.strip()
        print('line = ',line.strip())

        if line.endswith('row'):
            print('ROW!!')

        print('###########\n')
        with open('out.rtf','a') as outFile:
            if 'Client name' in line:
                print('setting skip_flag = 1')
                skip_flag = 1
            if 'Client ID' in line:
                print('setting skip_flag = 0')
                skip_flag = 0
            if skip_flag == 0:
                print('WILLLL write line = ',line)
                outFile.write(line+'\n')
